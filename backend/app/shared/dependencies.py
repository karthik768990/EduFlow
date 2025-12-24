from fastapi import Depends, HTTPException
from modules.auth.dependencies import get_current_user

def require_student(user=Depends(get_current_user)):
    if user.get("role") != "student":
        raise HTTPException(status_code=403, detail="Student only")
    return user

def require_teacher(user=Depends(get_current_user)):
    if user.get("role") != "teacher":
        raise HTTPException(status_code=403, detail="Teacher only")
    return user
