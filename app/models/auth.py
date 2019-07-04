from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base
from app import login_manager
from datetime import datetime


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    is_staff = Column(Boolean, default=False)

    @property
    def password(self):
        """
        获取密码
        :return:
        """
        return self._password

    @password.setter
    def password(self, raw):
        """
        设置密码
        :param raw:
        :return:
        """
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        """
        检查密码是否正确
        :param raw:
        :return:
        """
        return check_password_hash(self._password, raw)

    @property
    def now(self):
        return datetime.fromtimestamp(datetime.now().timestamp())


@login_manager.user_loader
def get_user(uid):
    """
    提供回调
    :param uid:
    :return:
    """
    return User.query.get(int(uid))

