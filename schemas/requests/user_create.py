from pydantic import BaseModel, EmailStr, constr

class UserCreateRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8)  # Requiere contraseña de mínimo 8 caracteres