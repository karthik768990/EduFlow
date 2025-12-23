from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.modules.auth.dependencies import get_current_user
from app.modules.users.service import UserService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/me")
def read_user(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return UserService.get_user(db, user["id"])
