from sqlalchemy import Column, Integer, String, DateTime

from backend.app.core.security import generate_jwt_token
from backend.app.database import Base
from datetime import datetime, timedelta

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)  # [[3]]
    token_expiration = Column(DateTime, nullable=True)

    def set_token(self):
        # Genera token con expiración de 1 año [[9]]
        self.token = generate_jwt_token(self.email)  # Implementación en security.py
        self.token_expiration = datetime.utcnow() + timedelta(days=365)