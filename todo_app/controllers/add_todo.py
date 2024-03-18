from fastapi import HTTPException
from todo_app.schema.todos import Todos

def add(data: Todos,session):
    with session:
        if data.content.strip():
            add: Todos = Todos(content=data.content)
            session.add(add)
            session.commit()
            session.refresh(add)
            return add
        else:
            raise HTTPException(status_code=404, detail="No data found")
        
def __repr__(self):
    return "<Todo (content={0}) >".format(self.content) 
