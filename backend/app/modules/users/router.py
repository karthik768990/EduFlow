from fastapi import APIRouter, Depends
from shared.dependencies import get_current_user
from sqlalchemy.orm import Session
from shared.db import get_db
from modules.users.service import UserService

router = APIRouter()

@router.post("/sync")
def sync_user(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return UserService.sync_user(db, current_user)
