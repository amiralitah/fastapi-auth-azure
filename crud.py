from sqlalchemy.orm import Session
from . import models

def get_user_auth_by_email(db: Session, email: str):
    return db.query(models.UserAuth).filter(models.UserAuth.provider_subject == email).first()

def create_user(db: Session, username, display_name, phone_number, email, password_hash):
    user = models.User(username=username, display_name=display_name, phone_number=phone_number)
    db.add(user)
    db.commit()
    db.refresh(user)

    auth = models.UserAuth(user_id=user.user_id, provider="local", provider_subject=email, password_hash=password_hash)
    db.add(auth)
    db.commit()
    db.refresh(auth)

    return user

def save_refresh_token(db: Session, user_id: str, token: str, expires_at):
    refresh_token = models.RefreshToken(user_id=user_id, token=token, expires_at=expires_at, is_revoked=False)
    db.add(refresh_token)
    db.commit()
    db.refresh(refresh_token)
    return refresh_token
