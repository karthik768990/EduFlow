from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.shared.db import get_db
from app.shared.dependencies import require_student
from app.modules.reflections.schemas import ReflectionCreate
from app.modules.reflections.service import ReflectionService

router = APIRouter()

@router.post("/")
def submit_reflection(
    payload: ReflectionCreate,
    db: Session = Depends(get_db),
    user=Depends(require_student)
):
    return ReflectionService.create(db, user["id"], payload.content)
