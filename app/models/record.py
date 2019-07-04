from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Record(Base):
    """
    考生档案
    """
    number = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    gender = Column("gender", Integer)
    age = Column(Integer)
    political = Column("political", Integer)
    is_current = Column("is_current", Integer)
    education = Column("education", Integer)
    origin = Column(String(50), nullable=False)
    major = Column(String(128), nullable=False)
    category = Column(String(128))
    student_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"))

    @property
    def get_gender(self):
        return "男" if self.gender == 0 else "女"

    @property
    def get_political(self):
        if self.political == 1:
            return "群众"
        elif self.political == 2:
            return "共青团员"
        else:
            return "中共党员"

    @property
    def get_is_current(self):
        return "是" if self.is_current == 1 else "否"

    @property
    def get_education(self):
        return "本科" if self.education == 0 else "专科"
