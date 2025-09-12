from dbcreate.engcreate import createDB
from CRUD.Add import *
from CRUD.Update import *
from CRUD.Delete import *
from CRUD.Get import *
from common.shared import *
from authorization.isAuthorized import *
from access.whoAccess import *

def main():
    # createDB()    #We only needed it the first time
    # AddAdmin()    #I have created one hard-coded admin just at first.
    while True:
        print("Login to our database.")
        name = get_string("Please enter your name: ")
        password = input("Please enter your password: ")

        admin = isAdmin(name, password)
        if admin:
            adminAccess()
            continue

        teacher = isTeacher(name, password)
        if teacher:
            teacherAccess()
            continue

        student = isStudent(name, password)
        if student:
            studentAccess(student.id, student.class_id)
            continue

        print("Invalid name or password!")




if __name__ == "__main__":
    main()
