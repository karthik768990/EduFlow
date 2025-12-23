from pydantic import BaseModel

class ReflectionCreate(BaseModel):
    content: str
