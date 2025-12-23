from fastapi import Depends, HTTPException
from modules.auth.dependencies import get_current_user
from shared.constants import ROLE_STUDENT, ROLE_TEACHER

def require_student(user=Depends(get_current_user)):
    if user["role"] != ROLE_STUDENT:
        raise HTTPException(status_code=403, detail="Student access only")
    return user


def require_teacher(user=Depends(get_current_user)):
    if user["role"] != ROLE_TEACHER:
        raise HTTPException(status_code=403, detail="Teacher access only")
    return user
