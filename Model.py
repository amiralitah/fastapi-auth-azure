from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from .database import Base

class User(Base):
    __tablename__ = "Users"
    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    display_name = Column(String)
    phone_number = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    auth = relationship("UserAuth", back_populates="user")

class UserAuth(Base):
    __tablename__ = "UserAuth"
    user_auth_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey("Users.user_id"))
    provider = Column(String, default="local")
    provider_subject = Column(String, unique=True)  # email
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="auth")

class RefreshToken(Base):
    __tablename__ = "RefreshTokens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey("Users.user_id"))
    token = Column(String, unique=True, nullable=False)
    expires_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_revoked = Column(Boolean, default=False)
