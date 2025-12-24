from sqlalchemy.orm import Session
from sqlalchemy import text

class RankingService:
    @staticmethod
    def get_leaderboard(db: Session):
        query = text("""
            SELECT user_id,
                   COUNT(*) AS completed
            FROM study_sessions
            WHERE ended_at IS NOT NULL
            GROUP BY user_id
            ORDER BY completed DESC
            LIMIT 10
        """)

        result = db.execute(query).mappings().all()

        return result
