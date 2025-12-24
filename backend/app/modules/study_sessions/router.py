from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.shared.db import get_db

from app.shared.dependencies import require_student
from app.modules.study_sessions.schemas import StudySessionStart
from app.modules.study_sessions.service import StudySessionService

router = APIRouter()

@router.post("/start")
def start_session(
    payload: StudySessionStart,
    db: Session = Depends(get_db),
    user=Depends(require_student)
):
    return StudySessionService.start(db, user["id"], payload.subject)

@router.post("/stop")
def stop_session(
    db: Session = Depends(get_db),
    user=Depends(require_student)
):
    session = StudySessionService.stop(db, user["id"])
    if not session:
        raise HTTPException(status_code=400, detail="No active session")
    return session
