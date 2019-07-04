from flask import request,redirect,url_for
from flask_login import current_user
from functools import wraps


# 装饰器 一定要会啊
def permission(func):
    """
    权限控制
    wraps 保存被装饰器装饰过的函数名
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_prefix = "admin" if current_user.is_staff else "student"
        if request.blueprint == user_prefix:
            return func(*args, **kwargs)
        else:
            return redirect(url_for(f'{user_prefix}.index'), 403)
    return wrapper
