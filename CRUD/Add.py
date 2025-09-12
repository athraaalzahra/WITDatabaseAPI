from sqlmodel import Session
from dbcreate.model import *
from dbcreate.engcreate import engine
from common.shared import get_string, get_digits, get_int
import bcrypt


def AddAdmin():
    name = get_string("Enter Admin Name: ")
    password = input("Enter Admin Password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())    #Encrypt the password before storing it.
    with Session(engine) as session:
        obj = Admin(name=name, password=hashed)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Admin Added: {obj.name}")

def AddStudent():
    name = get_string("Enter Student Name: ")
    password = input("Enter Student Password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    phone_num = get_digits("Enter Phone Number: ")
    age = get_int("Enter Student Age: ")
    class_id = get_int("Enter Student Class ID: ")

    with Session(engine) as session:
        obj = Student(name=name, password=hashed, phone_num=phone_num, age=age, class_id=class_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Student Added successfully")


def AddTeacher():
    name = get_string("Enter Teacher Name: ")
    password = input("Enter Teacher Password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    age = get_int("Enter Teacher Age: ")
    salary = get_digits("Enter Teacher Salary: ")
    subject_id = get_int("Enter Teacher Subject ID: ")

    with Session(engine) as session:
        obj = Teacher(name=name, password=hashed, age=age, salary=salary, subject_id=subject_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Teacher Added successfully.")


def AddClass():
    name = get_string("Enter Class Name: ")
    with Session(engine) as session:
        obj = Class(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Class Added successfully")


def AddSubject():
    name = get_string("Enter Subject Name: ")

    with Session(engine) as session:
        obj = Subject(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Subject Added successfully")


def AddGrade():
    with Session(engine) as session:
        grade_value = get_int("Enter the grade: ")
        student_id = get_int("Enter the student ID: ")
        subject_id = get_int("Enter the subject ID: ")

        student = session.get(Student, student_id)
        subject = session.get(Subject, subject_id)

        if not student:
            print("Student not found!")
            return
        if not subject:
            print("Subject not found!")
            return

        new_grade = Grade(
            grade=grade_value,
            student_id=student_id,
            subject_id=subject_id
        )
        session.add(new_grade)
        session.commit()
        session.refresh(new_grade)
        print("Grade added successfully.")



def AddClassTeacher():
    teacher_id = get_int("Enter Teacher ID: ")
    class_id = get_int("Enter Class ID: ")

    with Session(engine) as session:
        teacher = session.get(Teacher, teacher_id)
        class_ = session.get(Class, class_id)

        if not teacher:
            print("Teacher not found!")
            return
        if not class_:
            print("Class not found!")
            return

        obj = ClassTeacher(teacher_id=teacher_id, class_id=class_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"ClassTeacher Added successfully")
