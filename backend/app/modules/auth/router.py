from fastapi import APIRouter, Depends
from app.modules.auth.dependencies import get_current_user

router = APIRouter()

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    """
    Verifies Supabase token and returns authenticated user
    """
    return {
        "id": user["id"],
        "email": user["email"],
        "provider": user["app_metadata"]["provider"]
    }
