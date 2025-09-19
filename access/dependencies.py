from fastapi import HTTPException
from sqlmodel import Session, select
from dbcreate.engcreate import engine
from dbcreate.model import Admin, Teacher, Student
import bcrypt

def get_user_role(name: str, password: str):
    with Session(engine) as session:
        admin = session.exec(select(Admin).where(Admin.name == name)).first()
        if admin and bcrypt.checkpw(password.encode(), admin.password):
            return {"role": "admin", "user": admin}

        teacher = session.exec(select(Teacher).where(Teacher.name == name)).first()
        if teacher and bcrypt.checkpw(password.encode(), teacher.password):
            return {"role": "teacher", "user": teacher}

        student = session.exec(select(Student).where(Student.name == name)).first()
        if student and bcrypt.checkpw(password.encode(), student.password):
            return {"role": "student", "user": student}

    raise HTTPException(status_code=401, detail="Invalid username or password")
