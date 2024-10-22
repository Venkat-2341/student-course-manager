from sqlalchemy import Column, ForeignKey, String, INTEGER, Float, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from ..common import Base

class Courses(Base):
    __tablename__ = 'courses'
    course_id = Column(INTEGER, primary_key=True)
    course_name = Column(String(30), nullable=False, unique=True)
    description = Column(String(200), nullable=False)
    credits = Column(INTEGER, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")    
    
    def __repr__(self):
        return f"{self.course_id}:{self.course_name}, created_at:{self.created_at}, updated_at:{self.updated_at}"