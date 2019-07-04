from app.web import admin
from flask_login import login_required
from flask import render_template, request, flash, redirect, url_for
from app.utils.permission import permission
from app.models.record import Record
from sqlalchemy import or_
from flask import current_app
from app.forms.record import RecordUpdateForm
from app.forms.grade import GradeInputForm
from app.models.base import db
from app.models.grade import Grade
from app.models.admission import Admission
from app.forms.admission import AdmissionInputForm
from app.models.profession import Profession
from app.dto.admission import AdmissionDtoList
from app.dto.grade import GradeDtoList


@admin.route('/')
@login_required
@permission
def index():
    return render_template('admin/index.html')


@admin.route('/examinee/record', methods=['GET', 'POST'])
@login_required
@permission
def examinee_record():
    key = request.args.get('key', default="")
    page = request.args.get("page", type=int, default=1)
    if len(key) != 0:
        records = Record.query.filter(or_(Record.name.like(f"%{key}%"), Record.number.like(
            f"%{key}%"))).paginate(page, current_app.config["PER_PAGE"])
    else:
        records = Record.query.filter().paginate(page, current_app.config["PER_PAGE"])
    return render_template('admin/examinee_record.html', records=records, key=key)


@admin.route('/examinee/record/update/<int:record_id>', methods=['GET', 'POST'])
@login_required
@permission
def record_update(record_id):
    # form 和 request.form 不一样
    record = Record.query.get(record_id)
    form = RecordUpdateForm(formdata=request.form, obj=record)
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
        return redirect(url_for('admin.examinee_record'))
    return render_template('admin/record_update.html', form=form)


@admin.route('/examinee/record/delete/<int:record_id>', methods=['GET', 'POST'])
@login_required
@permission
def record_delete(record_id):
    record = Record.query.get(record_id)
    db.session.delete(record)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for('admin.examinee_record'))


@admin.route('/grade/input', methods=['GET', 'POST'])
@login_required
@permission
def grade_input_list():
    key = request.args.get('key', default="")
    page = request.args.get("page", type=int, default=1)
    if len(key) != 0:
        grade_list = Grade.query.filter(or_(Grade.name.like(f"%{key}%"), Grade.number.like(f"%{key}%")))
        record_list = Record.query.filter(or_(Record.name.like(f"%{key}%"), Record.number.like(f"%{key}%")))
    else:
        grade_list = Grade.query.filter()
        record_list = Record.query.filter()
    grades = GradeDtoList(grades=grade_list)
    grades.judge_records(records=record_list)
    return render_template('admin/grade_input_list.html', grades=grades, key=key)


@admin.route('/grade/input/add/<int:record_id>', methods=['GET', 'POST'])
@login_required
@permission
def grade_input_add(record_id):
    record = Record.query.get(record_id)
    form = GradeInputForm(formdata=request.form, obj=record)
    grade = Grade()
    if request.method == 'POST' and form.validate():
        grade.number = form.number.data
        grade.name = form.name.data
        grade.politics = form.politics.data
        grade.english = form.english.data
        grade.basis = form.basis.data
        grade.profession = form.profession.data
        grade.profession_basis = form.profession_basis.data
        db.session.add(grade)
        db.session.commit()
        flash("录入成功")
        return redirect(url_for('admin.grade_input_list'))
    return render_template('admin/grade_input_add.html', form=form)


@admin.route('/grade/input/update/<int:record_id>', methods=['GET', 'POST'])
@login_required
@permission
def grade_input_update(record_id):
    grade = Grade.query.get(record_id)
    form = GradeInputForm(formdata=request.form, obj=grade)
    if request.method == 'POST' and form.validate():
        grade.politics = form.politics.data
        grade.english = form.english.data
        grade.basis = form.basis.data
        grade.profession = form.profession.data
        grade.profession_basis = form.profession_basis.data
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for('admin.grade_input_list'))
    return render_template('admin/grade_input_update.html', form=form)


@admin.route('/admission/input', methods=['GET', 'POST'])
@login_required
@permission
def admission_input_list():
    key = request.args.get('key', default="")
    if len(key) != 0:
        admission_list = Admission.query.filter(Admission.number.like(f"%{key}%"))
        record_list = Record.query.filter(Record.number.like(f"%{key}%"))
    else:
        admission_list = Admission.query.all()
        record_list = Record.query.all()
    admissions = AdmissionDtoList(admissions=admission_list)
    admissions.judge_records(records=record_list)
    return render_template('admin/admission_input_list.html', admissions=admissions, key=key)


@admin.route('/admission/input/add/<int:record_id>', methods=['GET', 'POST'])
@login_required
@permission
def admission_input_add(record_id):
    record = Record.query.get(record_id)
    form = AdmissionInputForm(formdata=request.form, obj=record)
    admission = Admission()
    if request.method == 'POST' and form.validate():
        admission.number = form.number.data
        admission.unit = form.unit.data
        admission.re_subject = form.re_subject.data
        admission.re_grade = form.re_grade.data
        db.session.add(admission)
        db.session.commit()
        flash("录入成功")
        return redirect(url_for('admin.admission_input_list'))
    return render_template('admin/admission_input_add.html', form=form)


@admin.route('/admission/input/update/<int:record_id>', methods=['GET', 'POST'])
@login_required
@permission
def admission_input_update(record_id):
    admission = Admission.query.get(record_id)
    form = AdmissionInputForm(formdata=request.form, obj=admission)
    if request.method == 'POST' and form.validate():
        admission.unit = form.unit.data
        admission.re_subject = form.re_subject.data
        admission.re_grade = form.re_grade.data
        db.session.commit()
        flash("修改成功！")
        return redirect(url_for('admin.admission_input_list'))
    return render_template('admin/admission_input_update.html', form=form)


@admin.route('/grade/calculate')
@login_required
@permission
def grade_calculate():
    key = request.args.get('key', default="")
    if len(key) != 0:
        grades = Grade.query.filter(or_(Grade.number.like(f"%{key}%"), Grade.name.like(f"%{key}%")))
    else:
        grades = Grade.query.all()
    return render_template('admin/grade_calculate.html', grades=grades)


@admin.route('/admission/calculate')
@login_required
@permission
def admission_calculate():
    key = request.args.get('key', default="")
    admissions = Admission.query.all()
    records = Record.query.all()
    professions = Profession.query.all()
    return render_template('admin/admission_calculate.html', professions=professions,
                           records=records, admissions=admissions)
