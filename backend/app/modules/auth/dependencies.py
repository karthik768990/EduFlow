from fastapi import Header, HTTPException
from modules.auth.service import AuthService

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = authorization.replace("Bearer ", "")
    try:
        return AuthService.verify_supabase_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")
