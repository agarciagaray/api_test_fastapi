from backend.app.database.repositories.user_repository import UserRepository
from backend.app.database.models.user import User
from backend.app.core.security import generate_jwt_token
from backend.app.schemas.requests.auth import UserLoginRequest
from backend.app.schemas.requests.user_create import UserCreateRequest
from backend.app.core.security import hash_password, verify_password
from backend.app.database.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def create_user(user_data: UserCreateRequest) -> User:
        hashed_password = hash_password(user_data.password)  # [[1]]
        user = User(
            email=user_data.email,
            password_hash=hashed_password
        )
        return UserRepository.create(user)

    @staticmethod
    def authenticate_user(credentials: UserLoginRequest) -> User:
        user = UserRepository.get_by_email(credentials.username)
        if not user or not verify_password(credentials.password, user.password_hash):
            return None  # [[4]][[6]]
        return user