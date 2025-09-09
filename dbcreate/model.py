from sqlmodel import SQLModel, Field
class Student(SQLModel, table=True):  
        id: int = Field(primary_key=True, default=None)  
        name: str   
        phone_num: str   
        age: int 
        class_id: int = Field(foreign_key="class.id")   #class.id means the class named Class but SQLModel uses lowercase table's name.


class Teacher(SQLModel, table=True):
        id: int = Field(primary_key=True, default=None)
        name: str
        age: int
        salary: str
        subject_id: int = Field(foreign_key="subject.id") 


class Class(SQLModel, table=True):  
        # one to many (many students belong to one class)
        id: int = Field(primary_key=True, default=None)
        name: str 


class Subject(SQLModel, table=True):  
        id: int = Field(primary_key=True, default=None)
        name: str


class Grade(SQLModel, table=True):  
        # stores student grades for each subject
        id: int = Field(primary_key=True, default=None)
        grade: int
        student_id: int = Field(foreign_key="student.id")   # which student
        subject_id: int = Field(foreign_key="subject.id")   # which subject


class ClassTeacher(SQLModel, table=True):  
        # middle table to connect teacher with class (many-to-many relation)
        id: int = Field(primary_key=True, default=None)
        teacher_id: int = Field(foreign_key="teacher.id")   # which teacher
        class_id: int = Field(foreign_key="class.id")       # which class
        
