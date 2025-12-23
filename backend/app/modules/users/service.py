from .repository import UserRepository

class UserService:
    @staticmethod
    def get_user(db, user_id: str):
        return UserRepository.get_by_id(db, user_id)
