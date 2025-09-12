from sqlmodel import Session, select
from dbcreate.model import *
from dbcreate.engcreate import engine
import bcrypt
from access.whoAccess import *

def isAdmin(name, password):
    with Session(engine) as session:
        admin = session.exec(select(Admin).where(Admin.name == name)).first()
        if admin and bcrypt.checkpw(password.encode('utf-8'), admin.password):
            return admin
    return None

def isTeacher(name, password):
    with Session(engine) as session:
        teacher = session.exec(select(Teacher).where(Teacher.name == name)).first()
        if teacher and bcrypt.checkpw(password.encode('utf-8'), teacher.password):
            return teacher
    return None

def isStudent(name, password):
    with Session(engine) as session:
        student = session.exec(select(Student).where(Student.name == name)).first()
        if student and bcrypt.checkpw(password.encode('utf-8'), student.password):
            return student
    return None
