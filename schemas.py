from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSignup(BaseModel):
    username: str
    display_name: str
    phone_number: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshRequest(BaseModel):
    refresh_token: str
