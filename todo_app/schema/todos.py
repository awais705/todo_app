from sqlmodel import SQLModel, Field
from typing import Optional

class Todos(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)
    is_completed: Optional[bool] = Field(default=False)
