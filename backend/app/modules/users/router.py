# modules/users/router.py

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from supabase import create_client
import os
from dotenv import load_dotenv

from app.core.database import get_db
from app.modules.users.repository import UserRepository

load_dotenv()

router = APIRouter()

# Initialize Supabase client ONCE globally (Better for performance)
# Ideally, move this to a shared file like core/supabase.py later
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

# Check if env vars exist to prevent confusing 500 errors
if not supabase_url or not supabase_key:
    print("CRITICAL WARNING: Supabase URL or Key is missing in .env")


@router.post("/sync")
def sync_user(
    authorization: str | None  = Header(default= None),
    db: Session = Depends(get_db),
):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid header format")

    token = authorization.replace("Bearer ", "")

    try:
        # Instantiate client (or use a global instance)
        supabase = create_client(supabase_url, supabase_key)
        
        # Verify token
        # We wrap this in try-except because it raises an error on bad tokens
        response = supabase.auth.get_user(token)
        sb_user = response.user

        if not sb_user:
            raise HTTPException(status_code=401, detail="Invalid Supabase user")

    except Exception as e:
        # This catches "Signature has expired" or "Invalid token" errors
        print(f"Auth Error: {e}") 
        raise HTTPException(status_code=401, detail="Could not validate token")

    # Sync Logic
    user = UserRepository.get_by_id(db, sb_user.id)

    if not user:
        user = UserRepository.create(
            db,
            id=sb_user.id,
            email=sb_user.email,
            role="student",
        )

    return user