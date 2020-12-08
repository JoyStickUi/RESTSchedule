from flask import make_response, abort
from config import db
from models import Faculty, Teacher, Auditory, FacultySchema, TeacherSchema, AuditorySchema
from user import create_token

def read_all_fac():
