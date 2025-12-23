from sqlalchemy.orm import Session
from reflections.models import Reflection

class ReflectionRepository:

    @staticmethod
    def create(db: Session, reflection: Reflection):
        db.add(reflection)
        db.commit()
        db.refresh(reflection)
        return reflection
