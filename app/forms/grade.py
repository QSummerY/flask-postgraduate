from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange
from app.utils.widget import ReadOnlyInput


class GradeBaseFrom(Form):
    number = IntegerField(validators=[DataRequired()],
                          render_kw={'class': 'form-control', 'placeholder': '请输入考号'}, widget=ReadOnlyInput())
    name = StringField(validators=[DataRequired(), Length(2, 50)],
                       render_kw={'class': 'form-control', 'placeholder': '请输入姓名'}, widget=ReadOnlyInput())


class GradeSearchFrom(GradeBaseFrom):
    politics = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                            render_kw={'class': 'form-control', 'placeholder': '请输入政治成绩'}, widget=ReadOnlyInput())
    english = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                           render_kw={'class': 'form-control', 'placeholder': '请输入外语成绩'}, widget=ReadOnlyInput())
    basis = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                         render_kw={'class': 'form-control', 'placeholder': '请输入基础科目成绩'}, widget=ReadOnlyInput())
    profession_basis = IntegerField(validators=[DataRequired(), NumberRange(0, 100)], render_kw={
        'class': 'form-control', 'placeholder': '请输入专业基础科目成绩'}, widget=ReadOnlyInput())
    profession = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                              render_kw={'class': 'form-control', 'placeholder': '请输入专业科目成绩'}, widget=ReadOnlyInput())


class GradeInputForm(GradeBaseFrom):
    politics = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                            render_kw={'class': 'form-control', 'placeholder': '请输入政治成绩'})
    english = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                           render_kw={'class': 'form-control', 'placeholder': '请输入外语成绩'})
    basis = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                         render_kw={'class': 'form-control', 'placeholder': '请输入基础科目成绩'})
    profession_basis = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                                    render_kw={'class': 'form-control', 'placeholder': '请输入专业基础科目成绩'})
    profession = IntegerField(validators=[DataRequired(), NumberRange(0, 100)],
                              render_kw={'class': 'form-control', 'placeholder': '请输入专业科目成绩'})
