from flask import Flask
from flask_login import LoginManager
login_manager = LoginManager()

from app.models.base import db


def create_app():
    """
    创建flask核心对象app
    :return:
    """
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "请先登录或注册"

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    from app.web import auth, admin, student
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(student)
