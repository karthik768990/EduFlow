from sqlalchemy.orm import Session
from .models import Assignment

class AssignmentRepository:
    @staticmethod
    def create(db: Session, assignment: Assignment):
        db.add(assignment)
        db.commit()
        db.refresh(assignment)
        return assignment
