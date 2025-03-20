from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from backend.app.database.models.user import User
from backend.app.core.config import settings
from fastapi.security import OAuth2PasswordBearer
from backend.app.database.repositories.user_repository import UserRepository
from passlib.context import CryptContext  # [[1]][[9]]

# Define el esquema OAuth2 para extraer el token del header Authorization [[9]]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def generate_jwt_token(email: str) -> str:
    expires = datetime.utcnow() + timedelta(days=365)
    return jwt.encode(
        {"sub": email, "exp": expires},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def validate_token(token: str) -> bool:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return datetime.utcfromtimestamp(payload["exp"]) > datetime.utcnow()
    except JWTError:
        return False

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = UserRepository.get_by_token(token)
    if not user or not validate_token(user.token):
        raise HTTPException(401, "Token inválido o expirado")
    return user

# Configuración de hashing (PBKDF2-SHA256 con 260,000 iteraciones) [[8]]
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)