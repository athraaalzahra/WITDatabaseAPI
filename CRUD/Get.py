from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from dbcreate.engcreate import engine
from dbcreate.model import *
from access.dependencies import get_user_role

router = APIRouter()


@router.get("/admin/{name}/{password}")
def get_admin_by_id(admin_id: int, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can view admins")
    with Session(engine) as session:
        admin = session.get(Admin, admin_id)
        if not admin:
            raise HTTPException(status_code=404, detail="Admin not found")
        return {"id": admin.id, "name": admin.name}


@router.get("/admins/{name}/{password}")
def get_all_admins(user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can view admins")
    with Session(engine) as session:
        admins = session.exec(select(Admin).order_by(Admin.name)).all()
        return [{"id": a.id, "name": a.name} for a in admins]


@router.get("/student/{name}/{password}")
def get_student_by_id(student_id: int, user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher", "student"]:
        raise HTTPException(status_code=403, detail="Not authorized to view students")
    if user["role"] == "student" and user["id"] != student_id:
        raise HTTPException(status_code=403, detail="Students can only view their own info")
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "phone_num": student.phone_num,
            "class_id": student.class_id,
        }


@router.get("/students/{name}/{password}")
def get_all_students(user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not authorized to view all students")
    with Session(engine) as session:
        students = session.exec(select(Student).order_by(Student.name)).all()
        return [
            {"id": s.id, "name": s.name, "age": s.age, "phone_num": s.phone_num, "class_id": s.class_id}
            for s in students
        ]


@router.get("/teacher/{name}/{password}")
def get_teacher_by_id(teacher_id: int, user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not authorized to view teachers")
    with Session(engine) as session:
        teacher = session.get(Teacher, teacher_id)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return {
            "id": teacher.id,
            "name": teacher.name,
            "age": teacher.age,
            "salary": teacher.salary,
            "subject_id": teacher.subject_id,
        }


@router.get("/teachers/{name}/{password}")
def get_all_teachers(user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not authorized to view teachers")
    with Session(engine) as session:
        teachers = session.exec(select(Teacher).order_by(Teacher.name)).all()
        return [
            {"id": t.id, "name": t.name, "age": t.age, "salary": t.salary, "subject_id": t.subject_id}
            for t in teachers
        ]


@router.get("/class/{name}/{password}")
def get_class_by_id(class_id: int, user=Depends(get_user_role)):
    with Session(engine) as session:
        cls = session.get(Class, class_id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")
        return cls


@router.get("/class/student/{name}/{password}")
def get_class_by_studentID(student_id: int, user=Depends(get_user_role)):
    if user["role"] == "student" and user["id"] != student_id:
        raise HTTPException(status_code=403, detail="Cannot view other students' classes")
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        cls = session.get(Class, student.class_id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")
        return cls


@router.get("/classes/{name}/{password}")
def get_all_classes(user=Depends(get_user_role)):
    with Session(engine) as session:
        classes = session.exec(select(Class).order_by(Class.name)).all()
        return classes


@router.get("/subject/{name}/{password}")
def get_subject_by_id(subject_id: int, user=Depends(get_user_role)):
    with Session(engine) as session:
        subject = session.get(Subject, subject_id)
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        return subject


@router.get("/subjects/{name}/{password}")
def get_all_subjects(user=Depends(get_user_role)):
    with Session(engine) as session:
        subjects = session.exec(select(Subject).order_by(Subject.name)).all()
        return subjects


@router.get("/grades/student/{name}/{password}")
def get_grades_by_student(student_id: int, user=Depends(get_user_role)):
    if user["role"] == "student" and user["id"] != student_id:
        raise HTTPException(status_code=403, detail="Cannot view other students' grades")

    with Session(engine) as session:
        results = session.exec(
            select(Subject, Grade)
            .join(Subject, Grade.subject_id == Subject.id)
            .where(Grade.student_id == student_id)
            .order_by(Subject.name)
        ).all()
        return [{"subject": g[0].name, "grade": g[1].grade} for g in results]


@router.get("/teachers/class/{name}/{password}")
def get_teachers_by_class(class_id: int, user=Depends(get_user_role)):
    with Session(engine) as session:
        results = session.exec(
            select(Class.name, Teacher.name)
            .join(ClassTeacher, Class.id == ClassTeacher.class_id)
            .join(Teacher, ClassTeacher.teacher_id == Teacher.id)
            .where(Class.id == class_id)
            .order_by(Teacher.name)
        ).all()
        return [{"class_name": c, "teacher_name": t} for c, t in results]
