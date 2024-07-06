from pydantic import BaseModel
 
# Create ToDo Schema (Pydantic Model)
class MybookCreate(BaseModel):
    title: str
    author: str 
    description: str
 
# Complete ToDo Schema (Pydantic Model)
class Mybook(BaseModel):
    id: int
    title: str
    author: str 
    description: str
 
    class Config:
          from_attributes = True


class Deletebook(BaseModel):
    ok: bool