from CRUD.Add import *
from CRUD.Update import *
from CRUD.Delete import *
from CRUD.Get import *
from common.shared import *


def adminAccess():
    from main import main
    while True:
        print("\nChoose CRUD method:")
        print("(A) Add")
        print("(G) Get")
        print("(U) Update")
        print("(D) Delete")
        print("(O) Logout")

        CRUD = input("Enter your choice: ").upper().strip()

        match CRUD:
            case "A":  # Add
                while True:
                    print("\nADD Menu")
                    print("1. Add Admin")
                    print("2. Add Class")
                    print("3. Add Subject")
                    print("4. Add Student")
                    print("5. Add Teacher")
                    print("6. Add Grade")
                    print("7. Add ClassTeacher")
                    print("8. Exit Add menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": AddAdmin()
                        case "2": AddClass()
                        case "3": AddSubject()
                        case "4": AddStudent()
                        case "5": AddTeacher()
                        case "6": AddGrade()
                        case "7": AddClassTeacher()
                        case "8": break
                        case _: print("Invalid choice for Add — please enter 1–8.")

            case "G":  # Get
                while True:
                    print("\nGET Menu")
                    print("1. Get Admin by ID")
                    print("2. Get All Admins")
                    print("3. Get Student by ID")
                    print("4. Get All Students")
                    print("5. Get Teacher by ID")
                    print("6. Get All Teachers")
                    print("7. Get Class by ID")
                    print("8. Get All Classes")
                    print("9. Get Subject by ID")
                    print("10. Get All Subjects")
                    print("11. Get Grades by Student")
                    print("12. Get Teachers by Class")
                    print("13. Exit Get menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": get_admin_by_id(get_int("Enter admin ID: "))
                        case "2": get_all_admins()
                        case "3": get_student_by_id(get_int("Enter student ID: "))
                        case "4": get_all_students()
                        case "5": get_teacher_by_id(get_int("Enter teacher ID: "))
                        case "6": get_all_teachers()
                        case "7": get_class_by_id(get_int("Enter class ID: "))
                        case "8": get_all_classes()
                        case "9": get_subject_by_id(get_int("Enter subject ID: "))
                        case "10": get_all_subjects()
                        case "11": get_grades_by_student(get_int("Enter student ID: "))
                        case "12": get_teachers_by_class(get_int("Enter class ID: "))
                        case "13": break
                        case _: print("Invalid choice for Get — please enter 1–13.")

            case "U":  # Update
                while True:
                    print("\nUPDATE Menu")
                    print("1. Update Admin")
                    print("2. Change Password")
                    print("3. Update Class")
                    print("4. Update Subject")
                    print("5. Update Student")
                    print("6. Update Teacher")
                    print("7. Update Grade")
                    print("8. Update ClassTeacher")
                    print("9. Exit Update menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": UpdateAdmin()
                        case "2": changePassword()
                        case "3": UpdateClass()
                        case "4": UpdateSubject()
                        case "5": UpdateStudent()
                        case "6": UpdateTeacher()
                        case "7": UpdateGrade()
                        case "8": UpdateClassTeacher()
                        case "9": break
                        case _: print("Invalid choice for Update — please enter 1–9.")

            case "D":  # Delete
                while True:
                    print("\nDELETE Menu")
                    print("1. Delete Admin")
                    print("2. Delete Class")
                    print("3. Delete Subject")
                    print("4. Delete Student")
                    print("5. Delete Teacher")
                    print("6. Delete Grade")
                    print("7. Delete ClassTeacher")
                    print("8. Exit Delete menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": deleteAdmin()
                        case "2": deleteClass()
                        case "3": deleteSubject()
                        case "4": deleteStudent()
                        case "5": deleteTeacher()
                        case "6": deleteGrade()
                        case "7": deleteClassTeacher()
                        case "8": break
                        case _: print("Invalid choice for Delete — please enter 1–8.")

            case "O": 
                print("Logging out...")
                main()

            case _:
                print("Invalid CRUD choice! Please enter A, G, U, D, or E.")


def teacherAccess():
    from main import main
    while True:
        print("\nChoose CRUD method:")
        print("(A) Add")
        print("(G) Get")
        print("(U) Update")
        print("(D) Delete")
        print("(O) Logout")

        CRUD = input("Enter your choice: ").upper().strip()

        match CRUD:
            case "A":  # Add
                while True:
                    print("\nADD Menu")
                    print("1. Add Student")
                    print("2. Add Grade")
                    print("3. Exit Add menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": AddStudent()
                        case "2": AddGrade()
                        case "3": break
                        case _: print("Invalid choice for Add — please enter 1–3.")

            case "G":  # Get
                while True:
                    print("\nGET Menu")
                    print("1. Get Student by ID")
                    print("2. Get All Students")
                    print("3. Get Teacher by ID")
                    print("4. Get All Teachers")
                    print("5. Get Class by ID")
                    print("6. Get All Classes")
                    print("7. Get Subject by ID")
                    print("8. Get All Subjects")
                    print("9. Get Grades by Student")
                    print("10. Get Teachers by Class")
                    print("11. Exit Get menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": get_student_by_id(get_int("Enter student ID: "))
                        case "2": get_all_students()
                        case "3": get_teacher_by_id(get_int("Enter teacher ID: "))
                        case "4": get_all_teachers()
                        case "5": get_class_by_id(get_int("Enter class ID: "))
                        case "6": get_all_classes()
                        case "7": get_subject_by_id(get_int("Enter subject ID: "))
                        case "8": get_all_subjects()
                        case "9": get_grades_by_student(get_int("Enter student ID: "))
                        case "10": get_teachers_by_class(get_int("Enter class ID: "))
                        case "11": break
                        case _: print("Invalid choice for Get — please enter 1–11.")

            case "U":  # Update
                while True:
                    print("\nUPDATE Menu")
                    print("1. Update Class")
                    print("2. Update Subject")
                    print("3. Update Student")
                    print("4. Update Teacher")
                    print("5. Update Grade")
                    print("6. Update ClassTeacher")
                    print("7. Exit Update menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": UpdateClass()
                        case "2": UpdateSubject()
                        case "3": UpdateStudent()
                        case "4": UpdateTeacher()
                        case "5": UpdateGrade()
                        case "6": UpdateClassTeacher()
                        case "7": break
                        case _: print("Invalid choice for Update — please enter 1–7.")

            case "D":  # Delete
                while True:
                    print("\nDELETE Menu")
                    print("1. Delete Grade")
                    print("2. Exit Delete menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": deleteGrade()
                        case "2": break
                        case _: print("Invalid choice for Delete — please enter 1–2.")

            case "O": 
                print("Logging out...")
                main()

            case _:
                print("Invalid CRUD choice! Please enter A, G, U, D, or O.")

def studentAccess(student_id, class_id):
    from main import main
    while True:
        print("\nChoose CRUD method:")
        print("(G) Get")
        print("(O) Logout")

        CRUD = input("Enter your choice: ").upper().strip()

        match CRUD:
            case "G":  # Get
                while True:
                    print("\nGET Menu")
                    print("1. View My Grades")
                    print("2. View My Classes")
                    print("3. View My Subjects")
                    print("4. View My Teachers")
                    print("5. Exit Get menu")

                    CRUDchoice = input("Enter choice: ").strip()

                    match CRUDchoice:
                        case "1": get_grades_by_student(student_id)
                        case "2": 
                            get_class_by_studentID(student_id)
                        case "3":
                            get_all_subjects()
                        case "4": 
                            get_teachers_by_class(class_id)
                        case "5": break
                        case _: print("Invalid choice for Get — please enter 1–5.")

            case "O": 
                print("Logging out...")
                main()

            case _: 
                print("Invalid CRUD choice! Please enter G or O.")
