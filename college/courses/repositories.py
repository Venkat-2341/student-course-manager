from sqlalchemy.orm import Session
from . import models, schemas

class CoursesRepository:
    async def create(db:Session, course:schemas.CourseCreate):
        db_item = models.Courses(
            course_name = course.course_name,
            description = course.description,
            credits = course.credits,
            created_at = course.created_at,
            updated_at = course.updated_at
        )
        
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        return db_item
    
    def fetch_with_id(db:Session, _id):
        return db.query(models.Courses)\
            .filter(models.Courses.course_id == _id)\
                .first()
            
    def fetch_with_name(db: Session, name):
        return db.query(models.Courses)\
            .filter(models.Courses.course_name == name)\
                .first()
                
    def fetch_all(db:Session, skip:int=0, limit:int=10):
        return db.query(models.Courses)\
            .offset(skip)\
                .limit(limit)\
                    .all()
                    
     
    
    