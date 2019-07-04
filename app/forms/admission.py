from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange
from app.utils.widget import ReadOnlyInput


class AdmissionBaseForm(Form):
    number = IntegerField(validators=[DataRequired()],
                          render_kw={'class': 'form-control', 'placeholder': '请输入考号'}, widget=ReadOnlyInput())


class AdmissionSearchForm(AdmissionBaseForm):
    unit = StringField(validators=[DataRequired(), Length(2, 50)],
                       render_kw={'class': 'form-control', 'placeholder': '请输入录取单位'}, widget=ReadOnlyInput())
    re_subject = StringField(validators=[DataRequired(), Length(2, 50)],
                             render_kw={'class': 'form-control', 'placeholder': '请输入复试科目'}, widget=ReadOnlyInput())
    re_grade = IntegerField(validators=[DataRequired()],
                            render_kw={'class': 'form-control', 'placeholder': '请输入复试成绩'}, widget=ReadOnlyInput())


class AdmissionInputForm(AdmissionBaseForm):
    unit = StringField(validators=[DataRequired(), Length(2, 50)],
                       render_kw={'class': 'form-control', 'placeholder': '请输入录取单位'})
    re_subject = StringField(validators=[DataRequired(), Length(2, 50)],
                             render_kw={'class': 'form-control', 'placeholder': '请输入复试科目'})
    re_grade = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                            render_kw={'class': 'form-control', 'placeholder': '请输入复试成绩'})
