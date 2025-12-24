from sqlalchemy.orm import Session
from app.modules.doubts.models import AssignmentDoubt

class DoubtRepository:

    @staticmethod
    def create(db: Session, doubt: AssignmentDoubt):
        db.add(doubt)
        db.commit()
        db.refresh(doubt)
        return doubt

    @staticmethod
    def get_for_teacher(db: Session, teacher_id: str):
        return db.query(AssignmentDoubt)\
                 .filter(AssignmentDoubt.teacher_id == teacher_id)\
                 .order_by(AssignmentDoubt.created_at.desc())\
                 .all()
