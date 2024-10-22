from typing import List, Optional
from pydantic import BaseModel 
from sqlalchemy import DateTime, TIMESTAMP

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    date_of_birth: Optional[TIMESTAMP] = None
    created_at: Optional[DateTime] = None
    updated_at: Optional[DateTime] = None
    
class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id:int
    
    class Config():
        orm_mode = True


