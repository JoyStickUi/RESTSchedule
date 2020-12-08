from flask import make_response, abort
from config import db
from models import User, Faculty, Teacher, FacultySchema, TeacherSchema, Auditory, AuditorySchema
from user import create_token

def read_all_fac(token):
    user = User.query.filter(User.token == token).one_or_none()

    if user is not None:
        faculties = Faculty.query.order_by(Faculty.id).all()
        faculty_schema = FacultySchema(many=True)
        data = faculty_schema.dump(faculties).data
        return data
    else:
        abort(403, "Not allowed")

def read_one_fac(faculty_id, token):
    pass

def teachers(token):
    user = User.query.filter(User.token == token).one_or_none()

    if user is not None:
        teachers = Teacher.query.order_by(Teacher.id).all()
        teacher_schema = TeacherSchema(many=True)
        data = teacher_schema.dump(teachers).data
        return data
    else:
        abort(403, "Not allowed")

def auditory(token):
    user = User.query.filter(User.token == token).one_or_none()
    if user is not None:
        auditories = Auditory.query.order_by(Auditory.id).all()
        auditory_schema = AuditorySchema(many=True)
        data = auditory_schema.dump(auditories).data
        return data
    else:
        abort(403, "Not allowed")


