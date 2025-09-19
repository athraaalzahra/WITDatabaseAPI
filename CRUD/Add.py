from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from dbcreate.engcreate import engine
from dbcreate.model import *
import bcrypt
from access.dependencies import get_user_role
import re, unicodedata
IQ_11_AFTER_964 = re.compile(r'^\+964\d{11}$')

def _to_ascii_digits(s: str) -> str:
    out = []
    for ch in s:
        try:
            out.append(str(unicodedata.digit(ch)))  # handles Arabic/Indic digits too
        except (TypeError, ValueError):
            out.append(ch)
    return ''.join(out)

def normalize_phone_iq_11(raw: str) -> str:
    s = _to_ascii_digits(str(raw)).strip()
    s = re.sub(r"[ \-().]", "", s)  # drop separators

    # convert 00 to +
    if s.startswith("00"):
        s = "+" + s[2:]

    if s.startswith("+964"):
        rest = s[4:]
        if not rest.isdigit():
            raise HTTPException(status_code=422, detail="Phone must be +964 followed by digits only.")
        normalized = "+964" + rest
    elif s.startswith("964"):
        rest = s[3:]
        if not rest.isdigit():
            raise HTTPException(status_code=422, detail="Phone must be 964 followed by digits only.")
        normalized = "+964" + rest
    else:
        # treat as local; require exactly 11 digits (e.g., 0790xxxxxxx)
        if not s.isdigit() or len(s) != 11:
            raise HTTPException(status_code=422, detail="Local phone must be 11 digits (e.g., 0790xxxxxxx).")
        normalized = "+964" + s  # keep the leading 0 to make 11 after 964

    if not IQ_11_AFTER_964.match(normalized):
        raise HTTPException(status_code=422, detail="Phone must be +964 followed by exactly 11 digits.")
    return normalized



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
def add_student(
    sname: str,
    spassword: str,
    phone_num: str,
    age: int,
    class_id: int,
    user=Depends(get_user_role),
):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add students")

    phone_fixed = normalize_phone_iq_11(phone_num)  # always "+964" + 11 digits

    hashed = bcrypt.hashpw(spassword.encode("utf-8"), bcrypt.gensalt())
    with Session(engine) as session:
        cls = session.get(Class, class_id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")

        obj = Student(
            name=sname,
            password=hashed,
            phone_num=phone_fixed,
            age=age,
            class_id=class_id,
        )
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Student added successfully", "student_id": obj.id}
@router.post("/AddTeacher/{name}/{password}")
def add_teacher(sname: str, password: str, age: int, salary: float, subject_id: int,
                user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add teachers")

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    with Session(engine) as session:
        subject = session.get(Subject, subject_id)
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")

        obj = Teacher(name=sname, password=hashed, age=age, salary=salary, subject_id=subject_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Teacher added successfully", "teacher_id": obj.id}

@router.post("/AddClass/{name}/{password}")
def add_class(sname: str, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add classes")

    with Session(engine) as session:
        obj = Class(name=sname)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return {"message": "Class added successfully", "class_id": obj.id}

@router.post("/AddSubject/{name}/{password}")
def add_subject(sname: str, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can add subjects")

    with Session(engine) as session:
        obj = Subject(name=sname)
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