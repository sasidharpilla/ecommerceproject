from pydantic import BaseModel, EmailStr

# ✅ Register Schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    role: str = "user"  # Add role with default


# ✅ Login Schema (YOU MISSED THIS)
class UserLogin(BaseModel):
    email: str
    password: str