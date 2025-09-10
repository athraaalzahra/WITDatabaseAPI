from sqlmodel import create_engine,SQLModel
engine = create_engine("sqlite:///database.db")


def createDB():
        SQLModel.metadata.create_all(engine)
        print("database created successfully")