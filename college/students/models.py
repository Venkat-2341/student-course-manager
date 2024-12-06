from sqlalchemy import Column, INTEGER, String, TIMESTAMP, func, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from ..common import Base, db

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", INTEGER, ForeignKey("students.student_id")),
    Column("course_id", INTEGER, ForeignKey("courses.course_id"))
)

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
    courses = relationship('Courses', backref='students', secondary=student_course)

    def __repr__(self):
        return f"{self.student_id}: {self.first_name} {self.last_name}"
