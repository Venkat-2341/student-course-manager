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

    