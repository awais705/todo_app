from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from sqlmodel import Session
from typing import Annotated, Optional
from todo_app.controllers.create_table import create_table
from todo_app.schema.todos import Todos
from todo_app.controllers import get_all_todos,add_todo,update_todo,delete_todo
from todo_app.engine import engine


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_table()
    yield

app  =  FastAPI(
    lifespan=lifespan,
    title="Todo App with Fast API",
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ]
)

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def index():
    return {"message": "Welcome to Todo API Homepage"}  

#Get all todos  - Add query string to filter data by todo title
@app.get("/todos", response_model=list[Todos])
def todos(session: Annotated[Session, Depends(get_session)], q: Optional[str] = None):
    all_todos = get_all_todos.get_todos(session,q)
    return all_todos
    
# Add todo in todo list 
@app.post("/todo",response_model=Todos)
def add_todo_data(data: Todos, session: Annotated[Session, Depends(get_session)]):
    add =  add_todo.add(data,session)
    return add

# Update Todo list as per given ID and data
@app.put("/update/{id}",response_model=Todos)
def update_todo_by_id(id, post_data: Todos, session: Annotated[Session, Depends(get_session)]):
   update = update_todo.update(id,post_data, session)
   return update

# Delete Todo Lis as per given ID 
@app.delete("/delete/{id}")
def delete_todo_by_id(id: int,session: Annotated[Session, Depends(get_session)]):
    delete = delete_todo.delete(id,session)
    return delete
    

