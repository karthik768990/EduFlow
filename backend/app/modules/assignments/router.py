from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.modules.auth.dependencies import get_current_user
from .schemas import AssignmentCreate
from .service import AssignmentService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_assignment(
    payload: AssignmentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return AssignmentService.create(db, payload, user["id"])
    