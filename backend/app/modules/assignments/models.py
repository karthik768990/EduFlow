from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from core.database import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    subject = Column(String)
    deadline = Column(DateTime)
    created_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
