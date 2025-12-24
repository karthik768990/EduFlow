from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.shared.db import get_db
from app.modules.analytics.service import RankingService

router = APIRouter()

@router.get("/leaderboard")
def leaderboard(db: Session = Depends(get_db)):
    return RankingService.get_leaderboard(db)
