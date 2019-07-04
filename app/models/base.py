from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer
from datetime import datetime


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer, default=datetime.now().timestamp)
    status = Column(SmallInteger, default=1)

    @property
    def create_datetime(self):
        """
        时间戳转换
        :return:
        """
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        """
        删除操作
        :return:
        """
        self.status = 0

    # def set_attrs(self, attr_dict):
    #     """属性赋值"""
    #     for key, value in attr_dict.items():
    #         if hasattr(self, key) and key != 'id':
    #             setattr(self, key, value)


from app.models.auth import User
from app.models.record import Record
from app.models.grade import Grade
from app.models.admission import Admission
from app.models.profession import Profession
