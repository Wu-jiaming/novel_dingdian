from .sql import Sql
from dingdian.items import DingdianItem
from dingdian.items import  DcontentItem

class DingdianPipeline(object):
    def process_item(self, item, spider):
        if (isinstance(item, DingdianItem)):
            n_id = item['nameId']
            ret = Sql.select_name(n_id)
            if(ret[0] == 1):
                print("已经存在了")
                pass
            else:
                n_name = item['name']
                n_author = item['author']
                n_category = item['category']
                Sql.insert_dd_name(n_name, n_author, n_category, n_id)
                print("开始存小说列表")

        if (isinstance(item, DcontentItem)):
            url = item['chapter_url']
            num_id = item['num']
            name_id = item['chapter_content']
            chapter_name = item['chapter_name']
            chapter_content = item['chapter_content']
            Sql.insert_chapter_name(chapter_name, chapter_content, name_id, num_id, url)
            print("小说存储完毕")
            #return item

