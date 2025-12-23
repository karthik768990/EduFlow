from datetime import datetime
from modules.study_sessions.models import StudySession
from modules.study_sessions.repository import StudySessionRepository

class StudySessionService:

    @staticmethod
    def start(db, user_id: str, subject: str):
        session = StudySession(user_id=user_id, subject=subject)
        return StudySessionRepository.create(db, session)

    @staticmethod
    def stop(db, user_id: str):
        session = StudySessionRepository.get_active(db, user_id)
        if not session:
            return None
        session.end_time = datetime.utcnow()
        return StudySessionRepository.end_session(db, session)
