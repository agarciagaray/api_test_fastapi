# app/database/repositories/user_repository.py
from sqlalchemy.orm import Session
from backend.app.database.models.user import User
from backend.app.database import SessionLocal

class UserRepository:
    @staticmethod
    def get_by_id(user_id: int) -> User:
        db: Session = SessionLocal()
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_email(email: str) -> User:
        db: Session = SessionLocal()
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create(user: User) -> User:
        db: Session = SessionLocal()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update(user: User) -> User:
        db: Session = SessionLocal()
        db.commit()
        db.refresh(user)
        return user