from CRUD.Add import *
from CRUD.Update import *
from CRUD.Delete import *
from CRUD.Get import *
from common.shared import get_int

def main():
    while True:
        print("\nChoose CRUD method:")
        print("(A) Add")
        print("(G) Get")
        print("(U) Update")
        print("(D) Delete")
        print("(E) Exit")

        CRUD = input("Enter your choice: ").upper().strip()

        if CRUD == "A":     #Add
            while True: 
                print("\nADD Menu")
                print("1. Add Class")
                print("2. Add Subject")
                print("3. Add Student")
                print("4. Add Teacher")
                print("5. Add Grade")
                print("6. Add ClassTeacher")
                print("7. Exit Add menu")
                CRUDchoice = input("Enter choice: ").strip()

                if CRUDchoice == "1": AddClass()
                elif CRUDchoice == "2": AddSubject()
                elif CRUDchoice == "3": AddStudent()
                elif CRUDchoice == "4": AddTeacher()
                elif CRUDchoice == "5": AddGrade()
                elif CRUDchoice == "6": AddClassTeacher()
                elif CRUDchoice == "7": break
                else: print("Invalid choice for Add — please enter 1–7.")

        elif CRUD == "G":   #Get
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

                if CRUDchoice == "1":
                    get_student_by_id(get_int("Enter student ID: "))
                elif CRUDchoice == "2":
                    get_all_students()
                elif CRUDchoice == "3":
                    get_teacher_by_id(get_int("Enter teacher ID: "))
                elif CRUDchoice == "4":
                    get_all_teachers()
                elif CRUDchoice == "5":
                    get_class_by_id(get_int("Enter class ID: "))
                elif CRUDchoice == "6":
                    get_all_classes()
                elif CRUDchoice == "7":
                    get_subject_by_id(get_int("Enter subject ID: "))
                elif CRUDchoice == "8":
                    get_all_subjects()
                elif CRUDchoice == "9":
                    get_grades_by_student(get_int("Enter student ID: "))
                elif CRUDchoice == "10":
                    get_teachers_by_class(get_int("Enter class ID: "))
                elif CRUDchoice == "11":
                    break
                else:
                    print("Invalid choice for Get — please enter 1–11.")

        elif CRUD == "U":   #Update
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

                if CRUDchoice == "1": UpdateClass()
                elif CRUDchoice == "2": UpdateSubject()
                elif CRUDchoice == "3": UpdateStudent()
                elif CRUDchoice == "4": UpdateTeacher()
                elif CRUDchoice == "5": UpdateGrade()
                elif CRUDchoice == "6": UpdateClassTeacher()
                elif CRUDchoice == "7": break
                else: print("Invalid choice for Update — please enter 1–7.")

        elif CRUD == "D":   #Delete
            while True: 
                print("\nDELETE Menu")
                print("1. Delete Class")
                print("2. Delete Subject")
                print("3. Delete Student")
                print("4. Delete Teacher")
                print("5. Delete Grade")
                print("6. Delete ClassTeacher")
                print("7. Exit Delete menu")
                CRUDchoice = input("Enter choice: ").strip()

                if CRUDchoice == "1": deleteClass()
                elif CRUDchoice == "2": deleteSubject()
                elif CRUDchoice == "3": deleteStudent()
                elif CRUDchoice == "4": deleteTeacher()
                elif CRUDchoice == "5": deleteGrade()
                elif CRUDchoice == "6": deleteClassTeacher()
                elif CRUDchoice == "7": break
                else: print("Invalid choice for Delete — please enter 1–7.")

        
        elif CRUD == "E":   #Exit
            exit("!!!!!!!!GOODBYE!!!!!!!!!")

        else:
            print("Invalid input — please choose A, G, U, D, or E.")

if __name__ == "__main__":
    main()
