from sqlmodel import Session, select
<<<<<<< HEAD
from dbcreate.model import *
=======
from dbcreate.model import Student, Teacher, Class, Grade, Subject, ClassTeacher
>>>>>>> dfda6a2f97dbcf109d92dc486fc41a45edf6fb33
from dbcreate.engcreate import engine
import json

def get_student_by_id(student_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if student: 
            print(student)
        else:
            print("Not found!")

def get_all_students():
    with Session(engine) as session:
        students = session.exec(select(Student).order_by(Student.name)).all()
        for s in students:
            print(s)

def get_teacher_by_id(teacher_id: int):
    with Session(engine) as session:
        teacher = session.get(Teacher, teacher_id)
        if teacher: 
            print(teacher)
        else:
            print("Not found!")

def get_all_teachers():
    with Session(engine) as session:
        teachers = session.exec(select(Teacher).order_by(Teacher.name)).all()
        for t in teachers:
            print(t)

def get_class_by_id(class_id: int):
    with Session(engine) as session:
        cls = session.get(Class, class_id)
        if cls:
            print(cls)
        else:
            print("Not found!")

def get_all_classes():
    with Session(engine) as session:
        classes = session.exec(select(Class).order_by(Class.name)).all()
        for c in classes:
            print(c)

def get_subject_by_id(subject_id: int):
    with Session(engine) as session:
        sub = session.get(Subject, subject_id)
        if sub:
            print(sub)
        else:
            print("Subject not found!")

def get_all_subjects():
    with Session(engine) as session:
        subjects = session.exec(select(Subject).order_by(Subject.name)).all()
        for sub in subjects:
            print(sub)

def get_grades_by_student(student_id: int):
    with Session(engine) as session:
        results = session.exec(
            select(Grade, Subject)
            .join(Subject, Grade.subject_id == Subject.id)
            .where(Grade.student_id == student_id)
            .order_by(Subject.name)
        ).all()
        grades_list = [
            {"grade": g[0].grade, "subject": g[1].name} for g in results
        ]
        print(json.dumps(grades_list, indent=4))

def get_teachers_by_class(class_id: int):
    with Session(engine) as session:
        results = session.exec(
            select(ClassTeacher, Teacher)
            .join(Teacher, ClassTeacher.teacher_id == Teacher.id)
            .where(ClassTeacher.class_id == class_id)
            .order_by(Teacher.name)
        ).all()
        teachers_list = [t[1].name for t in results]
        print(teachers_list)