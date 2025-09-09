from sqlmodel import create_engine,SQLModel
engine = create_engine('sqlite:///database.db')


def createDb():
        SQLModel.metadata.create_all(engine)
        print("database created successfully")