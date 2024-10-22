from sqlalchemy import Column, INTEGER, String, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import Relationship
from ..common import Base

class Enrollments():
    __tablename__ = 'enrollments'
    enrollment_id = Column(INTEGER, primary_key=True)
    student_id = Column(INTEGER, ForeignKey('students.student_id'), nullable=False)
    course_id = Column(INTEGER, ForeignKey('courses.course_id'), nullable=False)
    enrollment_date = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    grade = Column(INTEGER)
    
    student = Relationship('Students', back_populates='enrollments')
    course = Relationship('Courses', back_populates='enrollments')
    
    def __repr__(self):
        return f"Enrollment(id={self.enrollment_id}, student_id={self.student_id}, course_id={self.course_id}, date={self.enrollment_date}, grade={self.grade})"