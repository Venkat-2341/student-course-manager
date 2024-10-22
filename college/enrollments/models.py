from sqlalchemy import Column, INTEGER, ForeignKey, TIMESTAMP, func, DateTime
from sqlalchemy.orm import relationship
from ..common import Base

class Enrollments(Base):
    __tablename__ = 'enrollments'

    enrollment_id = Column(INTEGER, primary_key=True)
    student_id = Column(INTEGER, ForeignKey('students.student_id'), nullable=False)
    course_id = Column(INTEGER, ForeignKey('courses.course_id'), nullable=False)
    enrollment_date = Column(DateTime(timezone=True), server_default=func.now())
    grade = Column(INTEGER)

    def __repr__(self):
        return (f"Enrollment(id={self.enrollment_id}, student_id={self.student_id}, "
                f"course_id={self.course_id}, date={self.enrollment_date}, grade={self.grade})")
