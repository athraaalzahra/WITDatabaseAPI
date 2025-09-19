from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from dbcreate.engcreate import engine
from dbcreate.model import *
import bcrypt
from access.dependencies import get_user_role


router = APIRouter() 
@router.post("/AddAdmin/{name}/{password}")
def add_admin(aName: str, aPassword: str, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add admins")

    hashed = bcrypt.hashpw(aPassword.encode('utf-8'), bcrypt.gensalt())
    with Session(engine) as session:
        obj = Admin(name=aName, password=hashed)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Admin added successfully", "admin_id": obj.id}

@router.post("/AddStudent/{name}/{password}")
def add_student(sname: str, spassword: str, phone_num: str, age: int, class_id: int,
                user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add students")

    hashed = bcrypt.hashpw(spassword.encode('utf-8'), bcrypt.gensalt())
    with Session(engine) as session:
        cls = session.get(Class, class_id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")

        obj = Student(name=sname, password=hashed, phone_num=phone_num, age=age, class_id=class_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Student added successfully", "student_id": obj.id}

@router.post("/AddTeacher/{name}/{password}")
def add_teacher(name: str, password: str, age: int, salary: float, subject_id: int,
                user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add teachers")

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    with Session(engine) as session:
        subject = session.get(Subject, subject_id)
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")

        obj = Teacher(name=name, password=hashed, age=age, salary=salary, subject_id=subject_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Teacher added successfully", "teacher_id": obj.id}

@router.post("/AddClass/{name}/{password}")
def add_class(name: str, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add classes")

    with Session(engine) as session:
        obj = Class(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Class added successfully", "class_id": obj.id}

@router.post("/AddSubject/{name}/{password}")
def add_subject(name: str, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add subjects")

    with Session(engine) as session:
        obj = Subject(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Subject added successfully", "subject_id": obj.id}

@router.post("/AddGrade/{name}/{password}")
def add_grade(grade_value: int, student_id: int, subject_id: int,
              user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Only admin or teacher can add grades")

    with Session(engine) as session:
        student = session.get(Student, student_id)
        subject = session.get(Subject, subject_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")

        grade = Grade(grade=grade_value, student_id=student_id, subject_id=subject_id)
        session.add(grade)
        session.commit()
        session.refresh(grade)
        return {"message": "Grade added successfully", "grade_id": grade.id}

@router.post("/AddClassTeacher/{name}/{password}")
def add_class_teacher(teacher_id: int, class_id: int,
                      user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add class-teacher assignments")

    with Session(engine) as session:
        teacher = session.get(Teacher, teacher_id)
        cls = session.get(Class, class_id)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")

        obj = ClassTeacher(teacher_id=teacher_id, class_id=class_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "ClassTeacher added successfully", "id": obj.id}
