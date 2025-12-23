from .models import Assignment
from .repository import AssignmentRepository

class AssignmentService:
    @staticmethod
    def create(db, data, teacher_id):
        assignment = Assignment(
            title=data.title,
            subject=data.subject,
            deadline=data.deadline,
            created_by=teacher_id
        )
        return AssignmentRepository.create(db, assignment)
