from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from dbcreate.engcreate import engine
from dbcreate.model import *
from access.dependencies import get_user_role

router = APIRouter()

confirm: bool = Query(default=False)

@router.delete("/DeleteAdmin/{name}/{password}")
def delete_admin(id: int, confirm: bool = False, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete admins")

    with Session(engine) as session:
        admin = session.get(Admin, id)
        if not admin:
            raise HTTPException(status_code=404, detail="Admin not found")
        if not confirm:
            return {"message": f"Add ?confirm=true to delete {admin.name}"}
        session.delete(admin)
        session.commit()
        return {"message": "Admin deleted successfully"}

@router.delete("/DeleteStudent/{name}/{password}")
def delete_student(id: int, confirm: bool = False, user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete students")

    with Session(engine) as session:
        student = session.get(Student, id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        if not confirm:
            return {"message": f"Add ?confirm=true to delete {student.name}"}
        session.delete(student)
        session.commit()
        return {"message": "Student deleted successfully"}

@router.delete("/DeleteTeacher/{name}/{password}")
def delete_teacher(id: int, confirm: bool = False, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete teachers")

    with Session(engine) as session:
        teacher = session.get(Teacher, id)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        if not confirm:
            return {"message": f"Add ?confirm=true to delete {teacher.name}"}
        session.delete(teacher)
        session.commit()
        return {"message": "Teacher deleted successfully"}

# ---------------- Class ----------------
@router.delete("/DeleteClass/{name}/{password}")
def delete_class(id: int, confirm: bool = False, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete classes")

    with Session(engine) as session:
        cls = session.get(Class, id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")
        if not confirm:
            return {"message": f"Add ?confirm=true to delete {cls.name}"}
        session.delete(cls)
        session.commit()
        return {"message": "Class deleted successfully"}

# ---------------- Subject ----------------
@router.delete("/DeleteSubject/{name}/{password}")
def delete_subject(id: int, confirm: bool = False, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete subjects")

    with Session(engine) as session:
        subject = session.get(Subject, id)
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        if not confirm:
            return {"message": f"Add ?confirm=true to delete {subject.name}"}
        session.delete(subject)
        session.commit()
        return {"message": "Subject deleted successfully"}

@router.delete("/DeleteGrade/{name}/{password}")
def delete_grade(id: int, confirm: bool = False, user=Depends(get_user_role)):
    if user["role"] not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete grades")

    with Session(engine) as session:
        grade = session.get(Grade, id)
        if not grade:
            raise HTTPException(status_code=404, detail="Grade not found")
        if not confirm:
            return {"message": "Add ?confirm=true to delete this grade"}
        session.delete(grade)
        session.commit()
        return {"message": "Grade deleted successfully"}

@router.delete("/DeleteClassTeacher/{name}/{password}")
def delete_ct(id: int, confirm: bool = False, user=Depends(get_user_role)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete ClassTeacher assignments")

    with Session(engine) as session:
        ct = session.get(ClassTeacher, id)
        if not ct:
            raise HTTPException(status_code=404, detail="ClassTeacher not found")
        if not confirm:
            return {"message": "Add ?confirm=true to delete this assignment"}
        session.delete(ct)
        session.commit()
        return {"message": "ClassTeacher deleted successfully"}
