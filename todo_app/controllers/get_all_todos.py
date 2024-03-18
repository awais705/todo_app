from sqlmodel import select
from todo_app.schema.todos import Todos

def get_todos(session,q):
    with session:
        if q : 
            statement = select(Todos).where(Todos.content == q)
            results = session.exec(statement)
        else:
            statement = select(Todos)
            results = session.exec(statement).all()
        
        
        
        if results == None:
            return {"message": "No data found"}

        data = [row for row in results]
        return data