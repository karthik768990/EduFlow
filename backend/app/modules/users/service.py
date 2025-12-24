from modules.users.repository import UserRepository
from modules.users.models import User

class UserService:

    @staticmethod
    def sync_user(db, supabase_user):
        user = UserRepository.get_by_id(db, supabase_user["id"])
        if user:
            return user

        new_user = User(
            id=supabase_user["id"],
            email=supabase_user["email"],
            role="student"  # default
        )
        return UserRepository.create(db, new_user)
