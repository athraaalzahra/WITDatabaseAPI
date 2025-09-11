from CRUD.Add import *
# from dbcreate.engcreate import createDB
from CRUD.Update import *
from CRUD.Delete import *
<<<<<<< HEAD
from CRUD.Get import *
def main():
    #createDB()
    print("The Database Has Been Created")
while True:
    print("Chose What CRUD Method You Want To Do")
    print("(A) for Add")
    print("(G) for get")
    print("(U) for updata")
    print("(D) for delete")
    print("(E) for exit ")
    CRUD=input("Enter Your CRUD Method").title().strip()
    if CRUD == "A":
        print("\n--- ADD Menu ---")
        print("1. Add Class")
        print("2. Add Subject")
        print("3. Add Student")
        print("4. Add Teacher")
        print("5. Add Grade")
        print("6. Add ClassTeacher")
        CRUDchoice = input("Enter CRUDchoice: ").strip()
    if CRUDchoice=="1":AddClass()
    elif CRUDchoice=="2":AddSubject()
    elif CRUDchoice=="3":AddStudent()
    elif CRUDchoice=="4":AddTeacher()
    elif CRUDchoice=="5":AddGrade()
    elif CRUDchoice=="6":AddClassTeacher()
    elif CRUD == "G":
        print("\n--- GET Menu ---")
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
        CRUDchoice = input("Enter choice: ").strip()

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
        
=======
# createDB()
 
# AddClass()          
# AddSubject()         
# AddStudent()
# AddTeacher() 
# AddGrade()        
# AddClassTeacher()
# UpdateGrade()
# UpdateStudent()
# deleteStudent()
deleteSubject()
>>>>>>> dfda6a2f97dbcf109d92dc486fc41a45edf6fb33
