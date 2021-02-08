from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, DateTime, Boolean, Column
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:root@localhost/school?charset=utf8')

Base = declarative_base()


class User(Base):
    __tablename__ = 'news_arche'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    create_at = Column(DateTime)
    is_valid = Column(Boolean)


# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class OpOrm:
    def __init__(self):
        self.session = Session()

    def insert(self):
        add_item = User(
                        title='你好',
                        create_at='2020-01-02',
                        is_valid=1
                        )
        self.session.add(add_item)
        self.session.commit()
        return add_item

    def find_one(self):
        data_one = self.session.query(User).get(1)
        return data_one

    def find_many(self):
        data_many = self.session.query(User).filter_by(title='你好')
        return data_many

    def update_one(self):
        up_one = self.session.query(User).get(1)
        if up_one:
            up_one.title = '屁屁西'
            self.session.add(up_one)
            self.session.commit()
        else:
            print('query error!')

    def update_many(self):
        up_many = self.session.query(User).filter(User.id > 3)
        if up_many:
            for i in up_many:
                i.is_valid = 0
                self.session.add(i)
            self.session.commit()
        else:
            print("query error!")

    def delete_one(self):
        delete_o = self.session.query(User).get(1)
        self.session.delete(delete_o)
        self.session.commit()


if __name__ == '__main__':
    init_oporm = OpOrm()
    # data = init_oporm.insert()
    # print(data.title)
    # one_item = init_oporm.find_one()
    # if one_item:
    #     print(one_item.title)
    # else:
    #     print("not exist")
    #
    # many_item = init_oporm.find_many()
    # print(many_item.count())
    # print(many_item)
    # init_oporm.delete_one()
    init_oporm.update_many()
