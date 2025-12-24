from pydantic import BaseModel

class DoubtCreate(BaseModel):
    assignment_id: int
    question: str
