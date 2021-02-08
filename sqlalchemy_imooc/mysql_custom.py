import MySQLdb


class MysqlCustom:
    """自定义的mysql数据库，可以实现简单的增删改查"""
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='root',
                db='school',
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print("Error: %s" % e)

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print("Error: %s" % e)

    def find_one(self):
        sql = "SELECT * FROM `news` WHERE `type` = %s ORDER BY `create_at` DESC;"
        cursor = self.conn.cursor()
        cursor.execute(sql, ('军事', ))
        res_data = cursor.fetchone()
        res_dict = dict(zip([i[0] for i in cursor.description], res_data))
        cursor.close()
        self.close_conn()
        return res_dict

    def find_many(self, pages, size):
        offset = (pages - 1) * size
        sql = "SELECT * FROM `news` WHERE `type` = %s ORDER BY `create_at` DESC LIMIT %s, %s;"
        cursor = self.conn.cursor()
        cursor.execute(sql, ('军事', offset, size))
        res_dict = [dict(zip([i[0] for i in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return res_dict

    def insert_one(self, item):
        try:
            sql = ("INSERT INTO `news` (`title`, `author`, `type`, `create_at`, `content`, `is_valid`)"
                   "VALUES (%s, %s, %s, %s, %s, %s);"
                   )
            cursor = self.conn.cursor()
            cursor.execute(sql, item)
            self.conn.commit()
        except MySQLdb.Error as e:
            print("Error: %s" % e)
            self.conn.rollback()
        finally:
            self.close_conn()


def main():
    m = MysqlCustom()
    # data = m.find_many(1, 5)
    # for i in data:
    #     print(i)
    m.insert_one(('标题1', 'lisa', '军事', '2020-02-02 02:02:02', "ppx", 1))


if __name__ == '__main__':
    main()



