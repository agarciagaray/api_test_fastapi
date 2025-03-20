from fastapi import APIRouter, Depends, HTTPException
from backend.app.schemas.requests.auth import UserLoginRequest
from backend.app.schemas.responses.token import TokenResponse
from backend.app.services.user_service import UserService
from backend.app.database.models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=TokenResponse)
async def register(user_data: UserCreateRequest):
    user = UserService.create_user(user_data)
    return TokenResponse(
        access_token=user.token,
        token_type="bearer",
        expires_at=user.token_expiration
    )


@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLoginRequest):
    user = UserService.authenticate_user(credentials)
    if not user:
        raise HTTPException(401, "Credenciales inválidas")

    # Si el token existe pero está vencido, se regenera [[9]]
    if user.token and not validate_token(user.token):
        user.set_token()
        UserService.update_user(user)

    return TokenResponse(
        access_token=user.token,
        token_type="bearer",
        expires_at=user.token_expiration
    )