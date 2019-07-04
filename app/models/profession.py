from sqlalchemy import Column, String, Integer, ForeignKey
from app.models.base import db


class Profession(db.Model):
    """
    专业字典
    """
    major_num = Column(Integer, primary_key=True)
    major_name = Column(String(50), nullable=False)
    in_plan = Column(Integer)
    out_plan = Column(Integer)
