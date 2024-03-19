from fastapi.testclient import TestClient
from sqlmodel import Field, Session, SQLModel, create_engine, select

# https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/#override-a-dependency

from todo_app.main import app
from todo_app.schema import todos

from todo_app import settings

# https://fastapi.tiangolo.com/tutorial/testing/
# https://realpython.com/python-assert-statement/
# https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/

# postgresql://ziaukhan:oSUqbdELz91i@ep-polished-waterfall-a50jz332.us-east-2.aws.neon.tech/neondb?sslmode=require

def test_read_main():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Todo API Homepage"}

# def test_write_main():
#     pass
#     connection_string = str(settings.connection_string).replace(
#     "postgresql", "postgresql+psycopg")

#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)  

#     with Session(engine) as session:  

#         def get_session_override():  
#                 return session  

        

#         client = TestClient(app=app)

#         todo_content = "Motivational Talks"

#         response = client.post("/todo/",
#             json={"content": todo_content}
#         )

#         data = response.json()

#         assert response.status_code == 200
#         assert data["content"] == todo_content
#         assert data["is_completed"] == False
  
def test_read_list_main():
    
    connection_string = str(settings.connection_string).replace(
    "postgresql", "postgresql+psycopg")

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        # app.dependency_overrides[get_session] = get_session_override 
        client = TestClient(app=app)

        response = client.get("/todos/")
        assert response.status_code == 200

# Test Case- Get Todo list with query parameters
def test_read_list_main_with_query_string():  
    connection_string = str(settings.connection_string).replace(
    "postgresql", "postgresql+psycopg")

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        # app.dependency_overrides[get_session] = get_session_override 
        client = TestClient(app=app)

        q = "buy bread"
        response = client.get("/todos/?q=buy bread")
        
        data = response.json()
        # print(response)
        assert response.status_code == 200
        assert data[0]["content"] == q
        assert data[0]["is_completed"] == False
        # assert response.json() == [{"id": 15, "is_completed": False,"content": "buy bread"}]


def test_update_todo_item():
    connection_string = str(settings.connection_string).replace(
    "postgresql", "postgresql+psycopg")

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        # app.dependency_overrides[get_session] = get_session_override 
        client = TestClient(app=app)

        id = 20
        todo_data = {
                    "content":"Late night",
                    "is_completed": True
                        }

        response = client.put("/update/20",json=todo_data)
        
        
        data = response.json()
        assert response.status_code == 200
        assert data["content"] == "Late night"
        assert data["is_completed"] == True
        assert data["id"] == id

def test_delete_todo_item():
    connection_string = str(settings.connection_string).replace(
    "postgresql", "postgresql+psycopg")

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        # app.dependency_overrides[get_session] = get_session_override 
        client = TestClient(app=app)

        id = 26
      

        response = client.delete("/delete/26")
        
        
        data = response.json()
        assert response.status_code == 200
        assert response.json() ==  {"status": "Todo Item is deleted successfully!"}
