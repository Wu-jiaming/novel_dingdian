import scrapy
from scrapy.http import Request
from dingdian.items import DingdianItem
from dingdian.items import DcontentItem
from pyquery import PyQuery as pq
from dingdian.mysqlpipelines.sql import Sql

class dingdianSpider(scrapy.Spider):
	name = 'dingdian'
	allowed_domains = ['www.23us.so']
	base_url = 'https://www.23us.so/list/'
	type_url = '.html'

	def start_requests(self):
		for i in range(1, 2):
			url = self.base_url + str(i) + '_1' + self.type_url
			yield Request(url, self.parse)
		#yield Request('https://www.23us.so/full.html', self.parse)

	def parse(self, response):
		#print(response.text)
		doc = pq(response.text)
		max_num = doc('#pagelink .last').text()
		#print("max_num:", max_num)
		base_url = response.url[:-6]
		#print("base_url:", base_url)
		#base_url: https://www.23us.so/list/1_
		# base_url: https://www.23us.so/list/2_
		# base_url: https://www.23us.so/list/3_
		# base_url: https://www.23us.so/list/4_
		# base_url: https://www.23us.so/list/5_
		# base_url: https://www.23us.so/list/6_
		# base_url: https://www.23us.so/list/7_
		# base_url: https://www.23us.so/list/8_
		# base_url: https://www.23us.so/list/9_
		# base_url: https://www.23us.so/ful
		for num in range(1, int(5)):
			url = base_url + str(num) + self.type_url
			yield Request(url, callback=self.get_name)

	def get_name(self, response):
		doc = pq(response.text)
		a_tags = doc('tr .L a').items()
		#i奇数是值小说名，i为偶数是最新章节
		i=1
		for a in a_tags:
			#print("==================")
			if(i % 2 == 1):
				novel_name = a.text()
				novel_url = a.attr('href')
				# print("小说名：", a.text())
				# print("小说的url：", a.attr('href'))
			else:
				novel_latest_chapter = a.text()
				novel_lc_url = a.attr('href')
				# print("小说最新章节：", a.text())
				# print("小说最新章节的url：", a.attr('href'))
			i = i + 1
			yield Request(novel_url, callback=self.get_chapter_url, 
								meta={'name': novel_name, 'url': novel_url})	
	
	def get_chapter_url(self, response):
		item = DingdianItem()
		#response.meta[key]：这个是提取从上一个函数传递下来的值。
		item['name'] = str(response.meta['name'])
		item['novel_url'] = str(response.meta['url'])
		doc = pq(response.text)
		#一次性获取所有td标签的里面的text文本
		tds = doc.find('td').text()
		#将文本str拆分成数组
		tds = tds.split(" ")
		novel_main_link = doc('.btnlinks a.read').attr('href')
		#category = tds[0].split("/")[-2] #根据url的特性分开，获取url上特殊的值
		category = tds[0]
		author = tds[1]
		serial_status = tds[2]
		serial_num = tds[4]
		#获取url的链接的特殊数字串
		nameId = novel_main_link.split("/")[-2]

		item['category'] = category
		item['author'] = author
		item['serial_status'] = serial_status
		item['serial_number'] = serial_num
		item['nameId'] = nameId
		#print("nameId:", nameId[-2])
		yield item
		yield Request(url=novel_main_link, callback=self.get_chapter, meta={'name_id': nameId})
		#print("item:", item)
		return item


	#获取章节内容
	def get_chapter(self, response):
		doc = pq(response.text)
		#response.encoding = 'utf-8'
		urls = doc('td.L a').items()
		#因为scrapy是异步抓取，章节是混乱的，需要给他有序的序列。用num识别
		num = 0
		for url in urls:
			num = num + 1
			chapter_url = url.attr('href')
			chapter_name = url.text()
			#print("url:", url.attr('href'))
			#print("text:", url.text())\
			#判断是否已经存在
			rets = Sql.select_chapter(chapter_url)
			if(rets[0] == 1):
				print("章节内容已经存在")
				pass
			else:
				yield Request(chapter_url, callback=self.get_chapter_content, meta={
					'num':num,
					'name_id':response.meta['name_id'],
					'chapter_name': chapter_name,
					'chapter_url': chapter_url
				})

	#获取每个章节的内容
	def get_chapter_content(self, response):
		item = DcontentItem()
		item['num'] = response.meta['num']
		item['name_id'] = response.meta['name_id']
		item['chapter_name'] = str(response.meta['chapter_name'])
		item['chapter_url'] = response.meta['chapter_url']
		doc = pq(response.text)
		content = doc('#contents').text()
		item['chapter_content'] = content
		#print("执行get_chapter_content")
		#print(content)
		#raise "end	"
		return item