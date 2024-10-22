from sqlalchemy import Column, INTEGER, String, TIMESTAMP, func, DateTime
from sqlalchemy.orm import relationship
from ..common import Base

class Students(Base):
    __tablename__ = 'students'

    student_id = Column(INTEGER, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(TIMESTAMP)  
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    enrollments = relationship('Enrollments', backref='student')

    def __repr__(self):
        return f"{self.student_id}: {self.first_name} {self.last_name}"
