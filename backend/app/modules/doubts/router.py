from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from shared.db import get_db
from shared.dependencies import require_student, require_teacher
from modules.doubts.schemas import DoubtCreate
from modules.doubts.service import DoubtService

router = APIRouter()

@router.post("/")
def post_doubt(
    payload: DoubtCreate,
    db: Session = Depends(get_db),
    user=Depends(require_student)
):
    return DoubtService.create_doubt(db, user["id"], payload)

@router.get("/teacher")
def view_doubts_for_teacher(
    db: Session = Depends(get_db),
    user=Depends(require_teacher)
):
    return DoubtService.get_teacher_doubts(db, user["id"])
