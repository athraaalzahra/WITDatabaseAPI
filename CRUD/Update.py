from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from dbcreate.engcreate import engine
from dbcreate.model import *
import bcrypt
from access.dependencies import get_user_role

router = APIRouter()

@router.put("/UpdateAdmin/{name}/{password}")
def update_admin(id: int, admin_update: Admin, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update admins")

    with Session(engine) as session:
        admin = session.get(Admin, id)
        if not admin:
            raise HTTPException(status_code=404, detail="Admin not found")
        admin.sqlmodel_update(admin_update.model_dump(exclude={"password", "id"}))
        session.commit()
        session.refresh(admin)
        return admin.model_dump(exclude={"password"})

@router.put("/UpdateStudent/{name}/{password}")
def update_student(id: int, student_update: Student, user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not authorized to update students")

    with Session(engine) as session:
        student = session.get(Student, id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        student.sqlmodel_update(student_update.model_dump(exclude={"password", "id"}))
        session.commit()
        session.refresh(student)
        return student.model_dump(exclude={"password"})

@router.put("/UpdateTeacher/{name}/{password}")
def update_teacher(id: int, teacher_update: Teacher, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update teachers")

    with Session(engine) as session:
        teacher = session.get(Teacher, id)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        teacher.sqlmodel_update(teacher_update.model_dump(exclude={"password", "id"}))
        session.commit()
        session.refresh(teacher)
        return teacher.model_dump(exclude={"password"})

@router.put("/UpdateClass/{name}/{password}")
def update_class(id: int, class_update: Class, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update classes")

    with Session(engine) as session:
        cls = session.get(Class, id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")
        cls.sqlmodel_update(class_update.model_dump(exclude={"id"}))
        session.commit()
        session.refresh(cls)
        return cls.model_dump()

@router.put("/UpdateSubject/{name}/{password}")
def update_subject(id: int, subject_update: Subject, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update subjects")

    with Session(engine) as session:
        subject = session.get(Subject, id)
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        subject.sqlmodel_update(subject_update.model_dump(exclude={"id"}))
        session.commit()
        session.refresh(subject)
        return subject.model_dump()

@router.put("/UpdateGrade/{name}/{password}")
def update_grade(id: int, grade_update: Grade, user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not authorized to update grades")

    with Session(engine) as session:
        grade = session.get(Grade, id)
        if not grade:
            raise HTTPException(status_code=404, detail="Grade not found")
        grade.sqlmodel_update(grade_update.model_dump(exclude={"id"}))
        session.commit()
        session.refresh(grade)
        return grade.model_dump()

@router.put("/UpdateClassTeacher/{name}/{password}")
def update_class_teacher(id: int, ct_update: ClassTeacher, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update ClassTeacher assignments")

    with Session(engine) as session:
        ct = session.get(ClassTeacher, id)
        if not ct:
            raise HTTPException(status_code=404, detail="ClassTeacher not found")
        ct.sqlmodel_update(ct_update.model_dump(exclude={"id"}))
        session.commit()
        session.refresh(ct)
        return ct.model_dump()

@router.put("/ChangePassword/{name}/{password}")
def change_password(username: str, new_password: str, confirm_password: str, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Cannot change other users' passwords")

    if new_password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    with Session(engine) as session:
        person = session.exec(select(Admin).where(Admin.name == username)).first()
        if not person:
            person = session.exec(select(Teacher).where(Teacher.name == username)).first()
        if not person:
            person = session.exec(select(Student).where(Student.name == username)).first()
        if not person:
            raise HTTPException(status_code=404, detail="No such person")

        hashed = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())
        person.password = hashed
        session.commit()
        return {"message": "Password changed successfully"}