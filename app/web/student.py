from app.models.base import db
from flask_login import login_required, current_user
from flask import render_template, request, flash
from app.utils.permission import permission
from app.forms.record import RecordAddForm, RecordUpdateForm
from app.models.record import Record
from app.web import student
from app.models.grade import Grade
from app.models.admission import Admission
from app.forms.grade import GradeSearchFrom
from app.forms.admission import AdmissionSearchForm


@student.route('/')
@login_required
@permission
def index():
    return render_template("student/index.html")


@student.route('/record/add', methods=['GET', 'POST'])
@login_required
@permission
def record_add():
    """
    档案填写
    :return:
    """
    db_record = Record.query.filter_by(student_id=current_user.id).first()
    form = RecordAddForm(request.form)

    if not db_record:
        if request.method == 'POST' and form.validate():
            record = Record()
            record.number = form.number.data
            record.name = form.name.data
            record.gender = form.gender.data
            record.is_current = form.is_current.data
            record.age = form.age.data
            record.origin = form.origin.data
            record.education = form.education.data
            record.political = form.political.data
            record.category = form.category.data
            record.major = form.major.data
            record.student_id = current_user.id
            db.session.add(record)
            db.session.commit()
            flash("档案填写成功！")
        print(form.errors)
    else:
        flash("请不要重复填写档案")
    return render_template("student/record_add.html", form=form)


@student.route('/record/update', methods=['GET', 'POST'])
@login_required
@permission
def record_update():
    # 表单是string 而模型是 int6
    record = Record.query.filter_by(student_id=current_user.id).first()
    form = RecordUpdateForm(obj=record, formdata=request.form)
    if request.method == "POST" and form.validate():
        record.name = form.name.data
        record.gender = form.gender.data
        record.is_current = form.is_current.data
        record.age = form.age.data
        record.origin = form.origin.data
        record.education = form.education.data
        record.category = form.category.data
        record.major = form.major.data
        record.political = form.political.data
        db.session.commit()
        flash("修改成功！")
    return render_template("student/record_update.html", form=form)


@student.route('/grade/query')
@login_required
@permission
def grade_query():
    record = Record.query.filter_by(student_id=current_user.id).first()
    student_number = record.number
    grade = Grade.query.get_or_404(student_number)
    form = GradeSearchFrom(obj=grade)
    return render_template('student/grade_query.html', form=form)


@student.route('/admission/query')
@login_required
@permission
def admission_query():
    record = Record.query.filter_by(student_id=current_user.id).first()
    student_number = record.number
    admission = Admission.query.get_or_404(student_number)
    form = AdmissionSearchForm(obj=admission)
    return render_template('student/admission_query.html', form=form)
