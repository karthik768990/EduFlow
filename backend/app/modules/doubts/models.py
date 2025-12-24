from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

class AssignmentDoubt(Base):
    __tablename__ = "assignment_doubts"

    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, nullable=False)
    student_id = Column(String, nullable=False)
    teacher_id = Column(String, nullable=False)
    question = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
