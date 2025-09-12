from sqlmodel import Session, select
from dbcreate.model import *
from dbcreate.engcreate import engine
from common.shared import get_string, get_digits, get_int
import bcrypt



def UpdateAdmin():
    with Session(engine) as session:
        adminID = get_int("Enter the admin's unique ID to update: ")
        admin = session.get(Admin, adminID)
        if admin is None:
            print("Admin not found!")
            return

        print(f"Current info:\nName: {admin.name}")

        newName, newPassword = admin.name, ""  #Keep password empty if not changed

        while True:
            choice = input("Update Name (N), Password (P), Exit (X): ").lower()
            match choice:
                case "n":
                    newName = get_string("Enter new name: ")
                case "p":
                    newPassword = input("Enter new password: ")
                case "x":
                    break
                case _:
                    print("Invalid option!")

        admin.name = newName
        if newPassword:  # Only update if password was changed
            admin.password = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())
        session.commit()
        print("Admin updated successfully.")



def changePassword():
    with Session(engine) as session:
        recordName = get_string("Enter the person you want to change the password for: ")

        # Search in Admin, Teacher, Student Tables:
        admin = session.exec(select(Admin).where(Admin.name == recordName)).first()
        if admin:
            person = admin
        else:
            teacher = session.exec(select(Teacher).where(Teacher.name == recordName)).first()
            if teacher:
                person = teacher
            else:
                student = session.exec(select(Student).where(Student.name == recordName)).first()
                if student:
                    person = student
                else:
                    print("No such person!")
                    return

        while True:
            newPassword = get_string("Enter the new password: ")
            confirmPassword = get_string("Confirm the changed password: ")
            if newPassword == confirmPassword:
                hashed = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())
                person.password = hashed
                session.commit()
                print("Password changed successfully.")
                break
            else:
                print("Passwords do not match! Try again.")


def UpdateStudent():
    with Session(engine) as session:
        studentID = get_int("Enter the student's unique ID to update: ")
        student = session.get(Student, studentID)
        if student is None:
            print("Student not found!")
            return

        print(f"Current info:\nName: {student.name}\nAge: {student.age}\nPhone: {student.phone_num}")

        newName, newAge, newPhone = student.name, student.age, student.phone_num

        while True:
            choice = input("Update Name (N), Age (A), Phone (P), Exit (X): ").lower()
            match choice:
                case "n":
                    newName = get_string("Enter new name: ")
                case "a":
                    newAge = get_int("Enter new age: ")
                case "p":
                    newPhone = get_digits("Enter new phone number: ")
                case "x":
                    break
                case _:
                    print("Invalid option!")

        student.name, student.age, student.phone_num = newName, newAge, newPhone
        session.commit()
        print("Student updated successfully.")


def UpdateTeacher():
    with Session(engine) as session:
        teacherID = get_int("Enter the teacher's ID to update: ")
        teacher = session.get(Teacher, teacherID)
        if teacher is None:
            print("Teacher not found!")
            return

        print(f"Current info:\nName: {teacher.name}\nAge: {teacher.age}\nSalary: {teacher.salary}")

        newName, newAge, newSalary = teacher.name, teacher.age, teacher.salary

        while True:
            choice = input("Update Name (N), Age (A), Salary (S), Exit (X): ").lower()
            match choice:
                case "n":
                    newName = get_string("Enter new name: ")
                case "a":
                    newAge = get_int("Enter new age: ")
                case "s":
                    newSalary = get_int("Enter new salary: ")
                case "x":
                    break
                case _:
                    print("Invalid option!")

        teacher.name, teacher.age, teacher.salary = newName, newAge, newSalary
        session.commit()
        print("Teacher updated successfully.")


def UpdateClass():
    with Session(engine) as session:
        classID = get_int("Enter class ID to update: ")
        cls = session.get(Class, classID)
        if cls is None:
            print("Class not found!")
            return

        print(f"Current class name: {cls.name}")
        newName = get_string("Enter new class name: ")
        cls.name = newName
        session.commit()
        print("Class updated successfully.")


def UpdateSubject():
    with Session(engine) as session:
        subjectID = get_int("Enter subject ID to update: ")
        sub = session.get(Subject, subjectID)
        if sub is None:
            print("Subject not found!")
            return

        print(f"Current subject name: {sub.name}")
        newName = get_string("Enter new subject name: ")
        sub.name = newName
        session.commit()
        print("Subject updated successfully.")


def UpdateGrade():
    with Session(engine) as session:
        gradeID = get_int("Enter grade ID to update: ")
        grade = session.get(Grade, gradeID)
        if grade is None:
            print("Grade not found!")
            return

        print(f"Current info:\nGrade: {grade.grade}\nStudent ID: {grade.student_id}\nSubject ID: {grade.subject_id}")
        newGrade = get_int("Enter new grade: ")
        grade.grade = newGrade
        session.commit()
        print("Grade updated successfully.")


def UpdateClassTeacher():
    with Session(engine) as session:
        ctID = get_int("Enter ClassTeacher ID to update: ")
        ct = session.get(ClassTeacher, ctID)
        if ct is None:
            print("Record not found!")
            return

        print(f"Current info:\nTeacher ID: {ct.teacher_id}\nClass ID: {ct.class_id}")
        newTeacherID = get_int("Enter new Teacher ID: ")
        newClassID = get_int("Enter new Class ID: ")

        ct.teacher_id = newTeacherID
        ct.class_id = newClassID
        session.commit()
        print("ClassTeacher updated successfully.")
