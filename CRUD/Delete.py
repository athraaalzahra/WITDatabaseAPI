from sqlmodel import Session
from dbcreate.model import Student, Teacher, Class, Subject, Grade, ClassTeacher
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
    
def deleteStudent():
    with Session(engine) as session:
        StudentName = get_string("Enter the student's name to delete: ")
        student = session.get(Student, StudentName)
        print(student)

        if not student:
            print("Student not found!")
            return
        
        session.delete(student)
        session.commit()
        print("Student deleted successfully")

