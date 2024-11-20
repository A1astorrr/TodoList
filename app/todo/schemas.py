from pydantic import BaseModel, ConfigDict

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False
    
class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoCreate):
    pass

class TodoUpdatePart(TodoCreate):
    title: str |  None = None
    description: str |  None = None
    completed: bool | None = None

class Todo(TodoBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int