from pydantic import BaseModel
from datetime import datetime

class AssignmentCreate(BaseModel):
    title: str
    subject: str
    deadline: datetime
