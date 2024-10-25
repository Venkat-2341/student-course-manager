from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class CourseBase(BaseModel):
    course_name: str
    description: str
    credits: int
    created_at: Optional[datetime] = None  # Use datetime here
    updated_at: Optional[datetime] = None  # Use datetime here
    
class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    course_id: int
    
    class Config:
        orm_mode = True