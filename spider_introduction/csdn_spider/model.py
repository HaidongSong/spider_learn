from peewee import *

db = MySQLDatabase("spider", host="127.0.0.1", port=3306, user="root", password='root')


class BaseModel(Model):
    class Meta:
        database = db
        table_name = 'ppx'

'''
char类型，要设置最大长度
对于无法确定长度的字段，可以设置为Text
'''


class Topic(BaseModel):
    title = CharField()
    id = TextField()
    csdn_id = IntegerField(primary_key=True)
    author = CharField()
    creat_time = DateTimeField()
    answer_nums = IntegerField(default=0)


if __name__ == '__main__':
    db.create_tables([Topic])

