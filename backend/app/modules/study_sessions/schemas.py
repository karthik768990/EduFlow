from pydantic import BaseModel
from datetime import datetime

class StudySessionStart(BaseModel):
    subject: str

class StudySessionEnd(BaseModel):
    end_time: datetime
