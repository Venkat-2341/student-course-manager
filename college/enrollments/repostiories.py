from sqlalchemy.orm import Session
from . import models, schemas

class EnrollmentRepository:
    async def create(db:Session, enrollment:schemas.EnrollmentCreate):
        db_item = models.Enrollments(
            student_id = enrollment.student_id,
            course_id = enrollment.course_id,
            enrollment_date = enrollment.enrollment_date,
            grade = enrollment.grade
        )
        
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        return 
    
    def delete(db:Session, enrollment:schemas.EnrollmentCreate):
        db_item = models.Enrollments()