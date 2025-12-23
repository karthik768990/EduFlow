from sqlalchemy.orm import Session
from study_sessions.models import StudySession

class StudySessionRepository:

    @staticmethod
    def create(db: Session, session: StudySession):
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def get_active(db: Session, user_id: str):
        return db.query(StudySession).filter(
            StudySession.user_id == user_id,
            StudySession.end_time.is_(None)
        ).first()

    @staticmethod
    def end_session(db: Session, session: StudySession):
        db.commit()
        db.refresh(session)
        return session
