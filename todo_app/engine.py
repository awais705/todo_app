from sqlmodel import create_engine
from todo_app.settings import connection_string


try:
    # recycle connections after 5 minutes
    # to correspond with the compute scale down
    engine =  create_engine(connection_string,echo= True, connect_args={"sslmode": "require"}, pool_recycle=300)
except :
    print("Not Connected")