from sqlalchemy.orm import Session
from . import models, schemas
from college.students.repositories import StudentRepository  
from college.courses.repositories import CoursesRepository 

class EnrollmentRepository:
    async def create(db:Session, enrollment:schemas.EnrollmentCreate):
        db_item = models.Enrollments(
            student_id = enrollment.student_id,
            course_id = enrollment.course_id,
            enrollment_date = enrollment.enrollment_date,
            grade = enrollment.grade
        )
        
        course = CoursesRepository.fetch_with_id(db, enrollment.course_id)
        student = StudentRepository.fetch_with_id(db, enrollment.student_id)
        
        student.courses.append(course)
        
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        return db_item
    
    def delete(db:Session, student_id:int, course_id:int):
        db_item = db.query(models.Enrollments)\
            .filter(models.Enrollments.student_id == student_id)\
                .filter(models.Enrollments.course_id == course_id)\
                    .first()
                    
        if db_item is None:
            return None
        
        db.delete(db_item)
        db.commit()
        
        return 
            
    def fetch_with_name(db:Session, student_id:int, course_id:int):
        db_item = db.query(models.Enrollments)\
            .filter(models.Enrollments.student_id == student_id)\
                .filter(models.Enrollments.course_id == course_id)\
                    .first()
        
        return db_item
    
    def fetch_all(db:Session, skip:int=0, limit:int=10):
        db_item = db.query(models.Enrollments)\
            .offset(skip)\
                .limit(limit)\
                    .all()
        
        return db_item