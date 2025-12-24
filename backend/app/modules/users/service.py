from modules.users.repository import UserRepository

class UserService:

    @staticmethod
    def sync_user(db, auth_user):
        email = auth_user.get("email")
        user_id = auth_user.get("sub")

        user = UserRepository.get_by_id(db, user_id)

        if not user:
            user = UserRepository.create(
                db,
                user_id=user_id,
                email=email,
                role="student",  # default
            )

        return user
