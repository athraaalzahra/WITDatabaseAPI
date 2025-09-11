from sqlmodel import Session

from dbcreate.model import *
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
        print(f"ClassTeacher Added: {obj}")
