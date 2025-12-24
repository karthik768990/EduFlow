from sqlalchemy.orm import Session
from study_sessions.models import StudySession
from assignments.models import Assignment

class RankingService:

    @staticmethod
    def get_leaderboard(db: Session):
        # demo logic (expand later)
        result = db.execute("""
            select user_id,
                   count(*) * 10 as score
            from study_sessions
            group by user_id
            order by score desc
            limit 10
        """)
        return result.fetchall()
