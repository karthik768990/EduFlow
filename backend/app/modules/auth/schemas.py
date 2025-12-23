from pydantic import BaseModel

class SupabaseToken(BaseModel):
    access_token: str
