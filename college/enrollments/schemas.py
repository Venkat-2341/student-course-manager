from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: Optional[datetime] = None  
    grade: Optional[int] = None
    
class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    enrollment_id: int
    
    class Config:
        orm_mode = True