
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import codecs
import json

import MySQLdb
from twisted.enterprise import adbapi


class ArticlespiderPipeline:
    def process_item(self, item, spider):
        return item


class MysqlPipelene:
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'root', 'article_spider', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into article_cnblogs(title, create_time, news_poster, content, tags, url, url_hash, front_image_url, front_image_path, digging_count, comment_nums, total_view)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE digging_count=VALUES(digging_count), comment_nums=VALUES(comment_nums), total_view=VALUES(total_view)
        """

        items_list = [item.get('title', ''), item.get('create_time', '1970-07-01'), item.get('news_poster', ''),
                      item.get('content', ''), item.get('tags', ''), item.get('url', ''), item.get('url_hash', ''),
                      ','.join(item.get('front_image_url', [])), item.get('front_image_path', ''),
                      item.get('digging_count', 0), item.get('comment_nums', 0), item.get('total_view', 0)]
        # image_path = ','.join(item.get('front_image_url', []))

        self.cursor.execute(insert_sql, tuple(items_list))
        self.conn.commit()

        return item


class MysqlTwistedPipeline:
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        from MySQLdb.cursors import DictCursor
        dbparms = dict(
            host=settings["HOST"],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            use_unicode=True,
            cursorclass=DictCursor,
        )
        # dbparms = dict(
        #     host='127.0.0.1',
        #     db='article_spider',
        #     user='root',
        #     passwd='root',
        #     charset='utf8',
        #     use_unicode=True,
        #     cursorclass=DictCursor,
        # )


        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparms)
        # dbpool = adbapi.ConnectionPool(
        #     'MySQLdb',
        #     host=settings["HOST"],
        #     db=settings['MYSQL_DB'],
        #     user=settings['MYSQL_USER'],
        #     passwd=settings['MYSQL_PASSWORD'],
        #     charset='utf8',
        #     use_unicode=True,
        #     cursorclass=DictCursor,)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql_t = """
            insert into article_cnblogs(title, create_time, news_poster, content, tags, url, url_hash, front_image_url, front_image_path, digging_count, comment_nums, total_view)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE digging_count=VALUES(digging_count), comment_nums=VALUES(comment_nums), total_view=VALUES(total_view)
        """

        items_list_t = [item.get('title', ''), item.get('create_time', '1970-07-01'), item.get('news_poster', ''),
                      item.get('content', ''), item.get('tags', ''), item.get('url', ''), item.get('url_hash', ''),
                      ','.join(item.get('front_image_url', [])), item.get('front_image_path', ''),
                      item.get('digging_count', 0), item.get('comment_nums', 0), item.get('total_view', 0)]

        cursor.execute(insert_sql_t, tuple(items_list_t))


class JsonEncodingPipeline:
    def __init__(self):
        self.file = codecs.open("article.json", "a", encoding="utf-8")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        front_image_path = ''
        if "front_image_url" in item:
            for _, value in results:
                front_image_path = value['path']
            item['front_image_path'] = front_image_path

        return item


