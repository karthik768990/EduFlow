from app.modules.doubts.models import AssignmentDoubt
from app.modules.doubts.repository import DoubtRepository
from app.modules.assignments.repository import AssignmentRepository

class DoubtService:

    @staticmethod
    def create_doubt(db, student_id, data):
        assignment = AssignmentRepository.get_by_id(db, data.assignment_id)

        doubt = AssignmentDoubt(
            assignment_id=data.assignment_id,
            student_id=student_id,
            teacher_id=assignment.created_by,
            question=data.question
        )
        return DoubtRepository.create(db, doubt)

    @staticmethod
    def get_teacher_doubts(db, teacher_id):
        return DoubtRepository.get_for_teacher(db, teacher_id)
