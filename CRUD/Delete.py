from sqlmodel import Session
from dbcreate.model import *
from dbcreate.engcreate import engine
from common.shared import get_string, get_digits, get_int

    
def sureDelete():
    while True:
            areSure = input("Are you sure you? (Y for Yes, N for No) ").lower().strip()
            if(areSure == 'y'):
                return True
            elif(areSure == 'n'):
                return False
            else:
                print("Please enter a valid option!")

def deleteStudent():
    with Session(engine) as session:
        studentID = get_int("Enter the student's ID to delete: ")
        student = session.get(Student, studentID)
        if not student:
            print("Student not found!")
            return
        if(sureDelete()):
            session.delete(student)
            session.commit()
            print("Student deleted successfully.")

def deleteTeacher():
    with Session(engine) as session:
        teacherID = get_int("Enter the teacher's ID to delete: ")
        teacher = session.get(Teacher, teacherID)
        if not teacher:
            print("Teacher not found!")
            return
        if(sureDelete()):
            session.delete(teacher)
            session.commit()
            print("Teacher deleted successfully.")

def deleteClass():
    with Session(engine) as session:
        classID = get_int("Enter the class ID to delete: ")
        cls = session.get(Class, classID)
        if not cls:
            print("Class not found!")
            return
        if(sureDelete()):
            session.delete(cls)
            session.commit()
            print("Class deleted successfully.")

def deleteSubject():
    with Session(engine) as session:
        subjectID = get_int("Enter the subject ID to delete: ")
        subject = session.get(Subject, subjectID)
        if not subject:
            print("Subject not found!")
            return
        if(sureDelete()):
            session.delete(subject)
            session.commit()
            print("Subject deleted successfully.")

def deleteGrade():
    with Session(engine) as session:
        gradeID = get_int("Enter the grade ID to delete: ")
        grade = session.get(Grade, gradeID)
        if not grade:
            print("Grade not found!")
            return
        if(sureDelete()):
            session.delete(grade)
            session.commit()
            print("Grade deleted successfully.")

def deleteClassTeacher():
    with Session(engine) as session:
        ctID = get_int("Enter the ClassTeacher ID to delete: ")
        ct = session.get(ClassTeacher, ctID)
        if not ct:
            print("ClassTeacher record not found!")
            return
        if(sureDelete()):
            session.delete(ct)
            session.commit()
            print("ClassTeacher deleted successfully.")