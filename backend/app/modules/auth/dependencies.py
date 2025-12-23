from fastapi import Header, HTTPException
from app.modules.auth.service import AuthService

def get_current_user(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    try:
        return AuthService.verify_supabase_token(token)
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")
