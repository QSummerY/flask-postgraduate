from app.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Grade(Base):
    """
    考生成绩
    """
    number = Column(Integer, ForeignKey('record.number', ondelete="CASCADE"), primary_key=True)
    name = Column(String(20), nullable=False)
    politics = Column(Integer, default=-1)
    english = Column(Integer, default=-1)
    basis = Column(Integer, default=-1)
    profession_basis = Column(Integer, default=-1)
    profession = Column(Integer, default=-1)

    @property
    def get_total(self):
        return self.politics+self.english+self.basis+self.profession_basis+self.profession

    @property
    def get_average(self):
        return (self.politics+self.english+self.basis+self.profession_basis+self.profession)/5
