from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import jwt
import os

from app.core.database import get_db
from app.modules.users.repository import UserRepository

security = HTTPBearer()
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

# ---------- AUTH ----------
from fastapi import Header, HTTPException
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY"),
)
def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = authorization.replace("Bearer ", "")

    try:
        res = supabase.auth.get_user(token)
        return res.user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


# ---------- ROLE GUARDS ----------
def require_student(user=Depends(get_current_user)):
    if user.role != "student":
        raise HTTPException(status_code=403, detail="Student only")
    return user


def require_teacher(user=Depends(get_current_user)):
    if user.role != "teacher":
        raise HTTPException(status_code=403, detail="Teacher only")
    return user
