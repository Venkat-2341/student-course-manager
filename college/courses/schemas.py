from typing import List, Optional
from pydantic import BaseModel 
from sqlalchemy import DateTime, TIMESTAMP

class CourseBase(BaseModel):
    
    course_name: str
    description: str
    credis: int
    created_at: Optional[DateTime] = None
    updated_at: Optional[DateTime] = None
    
class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    course_id: int
    
    class Config():
        orm_mode = True