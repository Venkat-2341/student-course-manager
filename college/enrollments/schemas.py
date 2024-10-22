from typing import List, Optional
from pydantic import BaseModel 
from sqlalchemy import DateTime, TIMESTAMP

class EnrollmentBase(BaseModel):
    
    student_id: int
    course_id: int
    enrollment_date = Optional[DateTime] = None
    grade = Optional[int] = None
    
class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    enrollment_id: int
    
    class Config():
        orm_mode = True

