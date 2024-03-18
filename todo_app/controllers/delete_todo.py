from fastapi import HTTPException
from sqlmodel import Session,select
from todo_app.engine import engine
from todo_app.schema.todos import Todos

def delete(id,session):
    with session:
        statement = select(Todos).where(Todos.id == id)
        results = session.exec(statement)
        todo_one = results.one()
        if todo_one is None:
            raise HTTPException(status_code=404, detail="Record doesn't exist")
        
        
        session.delete(todo_one)
        session.commit()

        print("Todo Deleted") 
        return {"status": "Todo Item is deleted successfully!"}