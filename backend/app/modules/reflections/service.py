from reflections.models import Reflection
from reflections.repository import ReflectionRepository

class ReflectionService:

    @staticmethod
    def create(db, user_id: str, content: str):
        reflection = Reflection(
            user_id=user_id,
            content=content
        )
        return ReflectionRepository.create(db, reflection)
