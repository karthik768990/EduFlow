from sqlalchemy import Column, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String)
    role = Column(String)  # student / teacher
