from sqlmodel import Session, select
from dbcreate.model import *
from dbcreate.model import *
from dbcreate.engcreate import engine


def get_admin_by_id(admin_id: int):
    with Session(engine) as session:
        admin = session.get(Admin, admin_id)
        if not admin:
            print("Not found!")
            return
        print(f"ID: {admin.id}\nName: {admin.name}")


def get_all_admins():
    with Session(engine) as session:
        admins = session.exec(select(Admin).order_by(Admin.name)).all()
        if not admins:
            print("There are no admins found!")
            return
        for a in admins:
            print(f"ID: {a.id}\nName: {a.name}")


def get_student_by_id(student_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            print("Not found!")
            return
        print(f"ID: {student.id}")
        print(f"Name: {student.name}")
        print(f"Age: {student.age}")
        print(f"Phone: {student.phone_num}")
        print(f"ClassID: {student.class_id}")


def get_all_students():
    with Session(engine) as session:
        students = session.exec(select(Student).order_by(Student.name)).all()
        if not students:
            print("There are no students found!")
            return
        for s in students:
            print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}, Phone: {s.phone_num}, ClassID: {s.class_id}")


def get_teacher_by_id(teacher_id: int):
    with Session(engine) as session:
        teacher = session.get(Teacher, teacher_id)
        if not teacher:
            print("Not found!")
            return
        print(f"ID: {teacher.id}")
        print(f"Name: {teacher.name}")
        print(f"Age: {teacher.age}")
        print(f"Salary: {teacher.salary}")
        print(f"SubjectID: {teacher.subject_id}")


def get_all_teachers():
    with Session(engine) as session:
        teachers = session.exec(select(Teacher).order_by(Teacher.name)).all()
        if not teachers:
            print("There are no teachers found!")
            return
        for t in teachers:
            print(f"ID: {t.id}, Name: {t.name}, Age: {t.age}, Salary: {t.salary}, SubjectID: {t.subject_id}")


def get_class_by_id(class_id: int):
    with Session(engine) as session:
        cls = session.get(Class, class_id)
        if not cls:
            print("Not found!")
            return
        print(cls)

def get_class_by_studentID(student_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            print("student not found!")
            return
        cls = session.get(Class, student.class_id)
        if not cls:
            print("Class not found!")
        print(cls)

def get_all_classes():
    with Session(engine) as session:
        classes = session.exec(select(Class).order_by(Class.name)).all()
        if not classes:
            print("There are no classes found!")
            return
        for c in classes:
            print(c)


def get_subject_by_id(subject_id: int):
    with Session(engine) as session:
        subject = session.get(Subject, subject_id)
        if not subject:
            print("Subject not found!")
            return
        print(subject)


def get_all_subjects():
    with Session(engine) as session:
        subjects = session.exec(select(Subject).order_by(Subject.name)).all()
        if not subjects:
            print("There are no subjects found!")
            return
        for sub in subjects:
            print(sub)


def get_grades_by_student(student_id: int):
    with Session(engine) as session:
        results = session.exec(
            select(Subject, Grade)
            .join(Subject, Grade.subject_id == Subject.id)
            .where(Grade.student_id == student_id)
            .order_by(Subject.name)
        ).all()
        grades_list = [
            {"subject": g[0].name, "grade": g[1].grade} for g in results
        ]
        student = session.get(Student, student_id)
        print(f"The grades that {student.name} has are:")
        for i in grades_list:
            print(f"{i['subject']}: {i['grade']}")

def get_teachers_by_class(class_id: int):
    with Session(engine) as session:
        results = session.exec(
            select(Class.name, Teacher.name)
            .join(ClassTeacher, Class.id == ClassTeacher.class_id)
            .join(Teacher, ClassTeacher.teacher_id == Teacher.id)
            .where(Class.id == class_id)
            .order_by(Teacher.name)
        ).all()
        print(results)
        for class_name, teacher_name in results:
            print(f"{class_name}: {teacher_name}")