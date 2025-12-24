from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import jwt
import os

from core.database import get_db
from modules.users.repository import UserRepository

security = HTTPBearer()
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

# ---------- AUTH ----------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            audience="authenticated",
        )

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=401, detail="User not synced")

        return user  # DB USER OBJECT

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
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
