from flask_login import login_user, logout_user, login_required
from app.forms.auth import RegisterForm, LoginForm
from app.web import auth
from flask import render_template, request, flash, redirect, url_for
from app.models.auth import User
from app.models.base import db


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash("注册成功")
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            user_prefix = "admin" if user.is_staff else "student"
            login_user(user, remember=True)
            next_url = request.args.get("next")
            print(next_url)
            if not next_url:
                next_url = f"{user_prefix}.index"
            return redirect(url_for(next_url))
        flash("用户不存在或密码错误")
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
