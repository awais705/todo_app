from sqlmodel import SQLModel
from todo_app import engine



def create_table():
    SQLModel.metadata.create_all(engine)