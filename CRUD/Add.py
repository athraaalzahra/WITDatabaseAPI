from sqlmodel import Session

from dbcreate.model import Student, Teacher, Class, Grade, Subject, ClassTeacher
from dbcreate.engcreate import engine




def get_string(prompt: str) -> str:
    value = input(prompt).strip().title()
    if value.isdigit():
        print("Invalid input! Please enter text only.")
        return get_string(prompt)
    return value

def get_digits(prompt: str) -> str:
    value = input(prompt).strip()
    if not value.isdigit():
        print("Invalid input! Please enter digits only.")
        return get_digits(prompt)
    return value

def get_int(prompt: str) -> int:
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return get_int(prompt)
    
def AddStudent():
    name = get_string("Enter Student Name: ")
    phone_num = get_digits("Enter Phone Number: ")
    age = get_int("Enter Student Age: ")
    class_id = get_int("Enter Student Class ID: ")

    with Session(engine) as session:
        obj = Student(name=name, phone_num=phone_num, age=age, class_id=class_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Student Added: {obj}")


def AddTeacher():
    name = get_string("Enter Teacher Name: ")
    age = get_int("Enter Teacher Age: ")
    salary = get_digits("Enter Teacher Salary: ")
    subject_id = get_int("Enter Teacher Subject ID: ")

    with Session(engine) as session:
        obj = Teacher(name=name, age=age, salary=salary, subject_id=subject_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Teacher Added: {obj}")


def AddClass():
    name = get_string("Enter Class Name: ")

    with Session(engine) as session:
        obj = Class(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Class Added: {obj}")


def AddSubject():
    name = get_string("Enter Subject Name: ")

    with Session(engine) as session:
        obj = Subject(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Subject Added: {obj}")


def AddGrade():
    grade = get_int("Enter Grade: ")
    student_id = get_int("Enter Student ID: ")
    subject_id = get_int("Enter Subject ID: ")

    with Session(engine) as session:
        obj = Grade(grade=grade, Student_id=student_id, subject_id=subject_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"Grade Added: {obj}")


def AddClassTeacher():
    teacher_id = get_int("Enter Teacher ID: ")
    class_id = get_int("Enter Class ID: ")

    with Session(engine) as session:
        obj = ClassTeacher(Teacher_id=teacher_id, class_id=class_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        print(f"ClassTeacher Added: {obj}")