import pymysql
from dingdian import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings. MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

db = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB, charset='utf8')
cur = db.cursor()

class Sql:
    @classmethod
    def insert_dd_name(cls, n_name, n_author, n_category, n_id):
        sql = "INSERT INTO novel_lists(`n_name`, `n_author`, `n_category`, `n_id`) values(%(n_name)s, %(n_author)s, %(n_category)s, %(n_id)s)"
        value = {
            'n_name' : n_name,
            'n_author' : n_author,
            'n_category' : n_category,
            'n_id' : n_id
        }
        try:
            cur.execute(sql, value)
            db.commit()
        except Exception as e:
            print("insert_dd_name error:", e)

    @classmethod
    def select_name(cls, n_id):
        sql = "select exists(select 1 from novel_lists where n_id = %(n_id)s)"
        value = {
            'n_id' : n_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def insert_chapter_name(cls, chapter_name, content, name_id, num_id, url):
        sql = 'insert into chapter(`chapter_name`, `content`, `name_id`, `num_id`, `url`) values(%(chapter_name)s, %(content)s, %(name_id)s, %(num_id)s, %(url)s)'
        value = {
            'chapter_name' : chapter_name,
            'content' : content,
            'name_id' : name_id,
            'num_id' : num_id,
            'url' : url
        }
        try:
            cur.execute(sql, value)
            db.commit()
        except Exception as e:
            print("insert_chapter_name error:", e)

    @classmethod
    def select_chapter(cls, url):
        sql = 'select exists(select 1 from chapter where url = %(url)s)'
        value = {'url' : url}
        cur.execute(sql, value)
        return cur.fetchall()[0]