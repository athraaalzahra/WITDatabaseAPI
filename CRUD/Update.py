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

def UpdateStudent():
    with Session(engine) as session:
        studentID = get_int("Enter the student's unique ID to update: ")
        student = session.get(Student, studentID)

        if student is None:
            print("The student is not found!")
            return

        print(f"Current info:\nName: {student.name}\nAge: {student.age}\nPhone: {student.phone_num}")

        newName, newAge, newPhone = student.name, student.age, student.phone_num

        while True:
            whichParam = input("Update Name (N), Age (A), Phone (P), Exit (X): ").lower()
            match whichParam:
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
        session.add(student)
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
            whichParam = input("Update Name (N), Age (A), Salary (S), Exit (X): ").lower()
            match whichParam:
                case "n":
                    newName = get_string("Enter new name: ")
                case "a":
                    newAge = get_int("Enter new age: ")
                case "s":
                    newSalary = get_string("Enter new salary: ")
                case "x":
                    break
                case _:
                    print("Invalid option!")

        teacher.name, teacher.age, teacher.salary = newName, newAge, newSalary
        session.add(teacher)
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
        session.add(cls)
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
        session.add(sub)
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
        session.add(grade)
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
        session.add(ct)
        session.commit()
        print("ClassTeacher updated successfully.")
