from sqlalchemy.orm import Session
from . import models, schemas

class StudentRepository:
    async def create(db: Session, student:schemas.StudentCreate):
        db_item = models.Students(
            first_name = student.first_name,
            last_name = student.last_name,
            email = student.email,
            date_of_birth = student.date_of_birth,
            created_at = student.created_at,
            updated_at = student.updated_at
        )
        
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        return db_item
    
    def fetch_with_id(db:Session, _id):
        return db.query(models.Students)\
            .filter(models.Students.student_id == _id)\
                .first()
                
    def fetch_with_name(db:Session, f_name, l_name):
        return db.query(models.Students)\
            .filter(models.Students.first_name == f_name)\
                .filter(models.Students.last_name == l_name)\
                    .first()
                
    def fetch_all(db:Session, skip:int=0, limit:int=10):
        return db.query(models.Students)\
            .offset(skip)\
                .limit(limit)\
                    .all()
                    

            
    