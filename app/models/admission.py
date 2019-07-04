from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base


class Admission(Base):
    """
    录取名单
    """
    number = Column(Integer, ForeignKey('record.number', ondelete="CASCADE"), primary_key=True)
    unit = Column(String(128), default=None)
    re_subject = Column(String(50), default=None)
    re_grade = Column(Integer, default=0)
