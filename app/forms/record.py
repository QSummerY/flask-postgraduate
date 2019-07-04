from wtforms import Form, StringField, IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange
from app.utils.record_map import gender_choice, political_choice, is_current_choice, education_choice
from app.utils.widget import ReadOnlyInput


class BaseRecordForm(Form):
    """
    档案验证的基类
    """
    name = StringField(validators=[DataRequired(), Length(2, 50)],
                       render_kw={'class': 'form-control', 'placeholder': '请输入姓名'})
    age = IntegerField(validators=[DataRequired(), NumberRange(15, 50)],
                       render_kw={'class': 'form-control', 'placeholder': '请输入年龄'})
    origin = StringField(validators=[DataRequired(), Length(2, 50)],
                         render_kw={'class': 'form-control', 'placeholder': '请输入来源'})
    category = StringField(validators=[DataRequired(), Length(2, 50)],
                           render_kw={'class': 'form-control', 'placeholder': '请输入专业类别'})
    major = StringField(validators=[DataRequired(), Length(2, 50)],
                        render_kw={'class': 'form-control', 'placeholder': '请输入报考专业'})
    gender = SelectField(u'gender', render_kw={'class': 'form-control', 'placeholder': '请选择性别'}, coerce=int)
    political = SelectField(u'political', render_kw={'class': 'form-control', 'placeholder': '请选择政治面貌'}, coerce=int)
    is_current = SelectField(u'is_current', render_kw={'class': 'form-control', 'placeholder': '请选择是否应届'}, coerce=int)
    education = SelectField(u'education', render_kw={'class': 'form-control', 'placeholder': '请选择学历'}, coerce=int)

    def __init__(self, *args, **kwargs):
        """
        super 执行父类的构造函数
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.gender.choices = gender_choice
        self.political.choices = political_choice
        self.is_current.choices = is_current_choice
        self.education.choices = education_choice


class RecordAddForm(BaseRecordForm):
    """
    填写档案
    """
    number = StringField(validators=[DataRequired(), Length(10, message="考号长度为10")],
                         render_kw={'class': 'form-control', 'placeholder': '请输入考号'})


class RecordUpdateForm(BaseRecordForm):
    number = IntegerField(validators=[DataRequired()],
                          render_kw={'class': 'form-control', 'placeholder': '请输入考号'}, widget=ReadOnlyInput())
