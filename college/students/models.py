from sqlalchemy import Column, INTEGER, String, Float, ForeignKey, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from ..common import Base

class Students(Base):
    student_id = Column(INTEGER, primary_key=True, nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(DateTime)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    
    def __repr__(self):
        return f"{self.student_id}:{self.first_name},created_at:{self.created_at}, updated_at:{self.updated_at} "