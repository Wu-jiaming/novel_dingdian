# from pyquery import PyQuery as  py
#
# doc = py('https://www.23us.so/xiaoshuo/22928.html', encoding="utf-8")
# novel_main_link = doc('.btnlinks a.read')
# print("novel_main_link:", novel_main_link.attr('href').split("/")[-2])
# tds = doc.find('td').text()
# tds = tds.split(" ")
# print("tds:", tds.eq(1).text())
# print("tds:", tds.eq(1).html())
# # print("tds:", tds.eq(1))
#
# print("tds:", doc.find('td').html())
# print("tds:", doc.find('td').text())
#
# print("tds:", doc('td').html())
# print("tds:", doc('td').text())
#
# print("tds[0]", tds[0])
# print("tds[1]", tds[1])
# print("tds[2]", tds[2])
# print("tds[3]", tds[3])
# print("tds[4]", tds[4])
# print("tds[5]", tds[5])
# print("tds[6]", tds[6])
# print("tds[7]", tds[7])


#----------------------------------------
# import pymysql
#
# db = pymysql.connect(host='localhost',user='root', password='123456', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

#-------------------
# -*- coding:utf-8 -*-
# import requests
# from pyquery import PyQuery as pq
# response = requests.get('https://www.23us.so/files/article/html/17/17865/index.html')
# response.encoding = 'utf-8'
# print(response.text)
# doc = pq(response.text.encode('utf-8').decode('utf-8'))
# #doc = pq('https://www.23us.so/files/article/html/17/17865/index.html', encoding='utf-8')
# urls = doc('td.L a').items()
# print("urls:", urls)
#
# with open('x.txt','w', encoding='utf-8') as f:
#     for url in urls:
#         print("url:", url.attr('href'))
#         print(type(url.text()))
#         print("text:", url.text())
#         f.write(url.text())
# f.close()

# for i in range(1,1):
#     print(i)
#二进制下载
# import requests
# import re
# response = requests.get('https://www.23us.so/files/article/html/17/17865/index.html')
# with open('sina.txt', 'wb') as f:
# 	f.write(response.content)

#编码为utf8在保存
import requests
import re
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

# response = requests.get('https://news.sina.com.cn/', headers=headers)
# if response.status_code == 200:
# 	print("成功")
# else:
# 	print("fail")
# response.encoding="utf-8"
# with open('sina.txt', 'w' ,encoding="utf-8") as f:
# 	f.write(response.text)

with open('sina.txt', 'r', encoding="utf-8") as f:
	doc = f.read()

doc="""<img src="//n.sinaimg.cn/news/521/w298h223/20180808/S9EJ-hhkuskt5130428.png" width="160" height="90"/>
<img src="//n.sinaimg.cn/news/521/w298h223/20180808/S9EJ-hhkuskt5130428.png" width="160" height="90"/>
<img src="//n.sinaimg.cn/news/521/w298h223/20180808/S9EJ-hhkuskt5130428.png" width="160" height="90"/>
"""
#img_pattern = re.compile('<a.*?href="(.*?)".*?>.*?<\/a>')
img_pattern = re.compile('<img.*?src="(.*?)".*?/>')
img_items = re.findall(img_pattern, doc)
#print("img_items:", img_items)
#for img in img_items:
	#print("img:", img)




email = "fixed-term.WU.Jia_ming@cn.bosch.com"
email_pattern = re.compile(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,10}$')
#email_pattern = re.compile(r'^[\w\d_-]+(\.[\w\d_-]+)*@[\w\d_-]+(\.[\w\d_-]+){0,10}$')
email_item = re.match(email_pattern, email)
#print(email_item.group())

#将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
hello_pattern = re.compile('hello')
#使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
hello = re.match(hello_pattern, 'hello')
#输出匹配的结果
#print(hello.group())
path = r"C:\mydir\myfile.txt\\"
#print(path)

re_pattern = re.compile(r'\d\\(\d)')
re_result = re.match(re_pattern, '3\8')
#print(re_result.group())

m = re.match('\bblow', 'blow') #'\bblow'，\b匹配后退键(Backspace)
if(m is not None):
	print("找到blow:", m.group())
else:
	print("找不到blow")

mm = re.match('\\bblow', 'blow') #'\\bblow'，\转义之后，\b是匹配单词边界
if(mm is not None):
	print("找到blow:", mm.group())
else:
	print("找不到blow")

mmm = re.match(r'\bblow', 'blow') #r'\bblow'原生字符串，\b匹配单词边界
if(mmm is not None):
	print("找到blow:", mmm.group())
else:
	print("找不到blow")
import numpy as np
x = np.zeros((5,))
print(x)