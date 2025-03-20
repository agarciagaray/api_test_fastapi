from fastapi import APIRouter, Depends, HTTPException
from backend.app.schemas.responses.user_response import UserResponse
from backend.app.services.user_service import UserService
from backend.app.core.security import get_current_user
from backend.app.database.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

# Ejemplo de endpoint protegido (requiere token válido)
@router.put("/update", response_model=UserResponse)
async def update_user(
    new_email: str,
    current_user: User = Depends(get_current_user)
):
    updated_user = UserService.update_user_email(current_user.id, new_email)
    return updated_user