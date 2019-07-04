from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
admin = Blueprint('admin', __name__, url_prefix='/admin')
student = Blueprint('student', __name__, url_prefix='/student')


from app.web.auth import *
from app.web.admin import *
from app.web.student import *
