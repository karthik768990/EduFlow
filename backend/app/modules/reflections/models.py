from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from core.database import Base

class Reflection(Base):
    __tablename__ = "reflections"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
