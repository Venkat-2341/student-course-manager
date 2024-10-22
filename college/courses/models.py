from sqlalchemy import Column, INTEGER, String, TIMESTAMP, func, DateTime
from sqlalchemy.orm import relationship
from ..common import Base

class Courses(Base):
    __tablename__ = 'courses'

    course_id = Column(INTEGER, primary_key=True)
    course_name = Column(String(30), nullable=False, unique=True)
    description = Column(String(200), nullable=False)
    credits = Column(INTEGER, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    enrollments = relationship('Enrollments', backref='course')

    def __repr__(self):
        return f"{self.course_id}: {self.course_name}"
