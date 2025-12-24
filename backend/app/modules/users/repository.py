from sqlalchemy.orm import Session
from modules.users.models import User

class UserRepository:

    @staticmethod
    def get_by_id(db: Session, user_id: str):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(db: Session, user_id: str, email: str, role: str):
        user = User(id=user_id, email=email, role=role)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
