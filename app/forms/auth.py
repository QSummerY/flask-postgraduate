from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.auth import User


class RegisterForm(Form):
    # form.errors
    email = StringField(validators=[DataRequired(), Length(8, 64),
                        Email(message="电子邮箱不符合规范")], render_kw={'class': "form-control", 'placeholder': "请输入邮箱！"})

    password = PasswordField(validators=[
        DataRequired(message="密码不可以为空，请输入你的密码"), Length(6, 25)], render_kw={'class': "form-control", 'placeholder': "请输入密码！"})

# 自定义　error 需要到 form.email.error
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            # print("电子邮件已被注册")
            raise ValidationError("电子邮件已被注册")


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                        Email(message="电子邮箱不符合规范")], render_kw={'class': "form-control", 'placeholder': "请输入邮箱！"})

    password = PasswordField(validators=[
        DataRequired(message="密码不可以为空，请输入你的密码"), Length(6, 25)], render_kw={'class': "form-control", 'placeholder': "请输入密码！"})
