from pydantic import BaseModel

class UserLoginRequest(BaseModel):
    username: str  # Usado como email
    password: str