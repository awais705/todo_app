from fastapi import HTTPException
from sqlmodel import select
from todo_app.schema.todos import Todos

def update(id, post_data,session):
    with session:
        statement = select(Todos).where(Todos.id == id)
        results = session.exec(statement)
        todo_one = results.one()
        if todo_one is None:
            raise HTTPException(status_code=404, detail="Record doesn't exist")
        
        # for row in result:
        #     content,iscompleted = (row.content,row.is_completed)

        # print(result.is_completed)
        # if post_data.content is None:
        #     post_data.content = result.content

        if post_data.is_completed is not None and post_data.is_completed != todo_one.is_completed:
            todo_one.is_completed = post_data.is_completed
        
        if post_data.content is not None and post_data.content != todo_one.content:
            todo_one.content = post_data.content

            # session.add(todo_one)

            session.commit()
            session.refresh(todo_one)

            print("Updated Todo :", todo_one) 
            return todo_one