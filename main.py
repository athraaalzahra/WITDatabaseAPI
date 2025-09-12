from CRUD.Add import *
# from dbcreate.engcreate import createDB
from CRUD.Update import *
from CRUD.Delete import *
from CRUD.Get import *
def main():
    #createDB()
    print("The Database Has Been Created")
while True:
        print("Chose What CRUD Method You Want To Do: ")
        print("(A) for Add")
        print("(G) for Get")
        print("(U) for Update")
        print("(D) for Delete")
        print("(E) for Exit ")
        CRUD = input("Enter Your CRUD Method: ").upper().strip()

        if CRUD == "A":
            print("ADD Menu ")
            print("1. Add Class")
            print("2. Add Subject")
            print("3. Add Student")
            print("4. Add Teacher")
            print("5. Add Grade")
            print("6. Add ClassTeacher")
            print("7. Exit ")
            CRUDchoice = input("Enter choice CRUD: ").strip()   # keep as string!

            if CRUDchoice == "1": AddClass()
            elif CRUDchoice == "2": AddSubject()
            elif CRUDchoice == "3": AddStudent()
            elif CRUDchoice == "4": AddTeacher()
            elif CRUDchoice == "5": AddGrade()
            elif CRUDchoice == "6": AddClassTeacher()
            elif CRUDchoice == "7": exit("GOODBYE!")
            else: 
                print("Invalid choice (enter a number) for Add")

        elif CRUD == "G":
            print("GET Menu: ")
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
            print("11. Exit")
            CRUDchoice = input("Enter choice CRUD: ").strip()

            if CRUDchoice == "1": get_student_by_id(int(input("Enter student ID: ")))
            elif CRUDchoice == "2": get_all_students()
            elif CRUDchoice == "3": get_teacher_by_id(int(input("Enter teacher ID: ")))
            elif CRUDchoice == "4": get_all_teachers()
            elif CRUDchoice == "5": get_class_by_id(int(input("Enter class ID: ")))
            elif CRUDchoice == "6": get_all_classes()
            elif CRUDchoice == "7": get_subject_by_id(int(input("Enter subject ID: ")))
            elif CRUDchoice == "8": get_all_subjects()
            elif CRUDchoice == "9": get_grades_by_student(int(input("Enter student ID: ")))
            elif CRUDchoice == "10": get_teachers_by_class(int(input("Enter class ID: ")))
            elif CRUDchoice == "11": exit("GOODBYE!")
            else: 
                print("Invalid choice for Get")

        elif CRUD == "U":
            print("UPDATE Menu ")
            print("1. Update Class")
            print("2. Update Subject")
            print("3. Update Student")
            print("4. Update Teacher")
            print("5. Update Grade")
            print("6. Update ClassTeacher")
            print("7. Exit")
            CRUDchoice = input("Enter choice CRUD: ").strip()

            if CRUDchoice == "1": UpdateClass()
            elif CRUDchoice == "2": UpdateSubject()
            elif CRUDchoice == "3": UpdateStudent()
            elif CRUDchoice == "4": UpdateTeacher()
            elif CRUDchoice == "5": UpdateGrade()
            elif CRUDchoice == "6": UpdateClassTeacher()
            elif CRUDchoice == "7": exit("GOODBYE!")
            else: 
                print("Invalid choice for Update")

        elif CRUD == "D":
            print("DELETE Menu ")
            print("1. Delete Class")
            print("2. Delete Subject")
            print("3. Delete Student")
            print("4. Delete Teacher")
            print("5. Delete Grade")
            print("6. Delete ClassTeacher")
            print("7. Exit")
            CRUDchoice = input("Enter choice CRUD: ").strip()

            if CRUDchoice == "1": deleteClass()
            elif CRUDchoice == "2": deleteSubject()
            elif CRUDchoice == "3": deleteStudent()
            elif CRUDchoice == "4": deleteTeacher()
            elif CRUDchoice == "5": deleteGrade()
            elif CRUDchoice == "6": deleteClassTeacher()
            elif CRUDchoice == "7": exit("GOODBYE!")
            else: 
                print("Invalid choice for Delete")

        elif CRUD == "E":
            exit("!!!!!!!!GOODBYE!!!!!!!!!")
        else:
            print("Please write valid input :( ")




        
