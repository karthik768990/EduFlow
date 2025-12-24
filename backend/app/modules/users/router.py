from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.auth.dependencies import get_current_user
from shared.db import get_db
from modules.users.service import UserService

router = APIRouter()

@router.post("/sync")
def sync_user(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return UserService.sync_user(db, user)
