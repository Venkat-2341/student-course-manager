from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Student Schemas
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    date_of_birth: Optional[datetime] = None  
    created_at: Optional[datetime] = None  
    updated_at: Optional[datetime] = None  
    
class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int
    
    class Config:
        orm_mode = True