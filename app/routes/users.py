import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["Users"])

logger = logging.getLogger(__name__)


# -----------------------------
# REGISTER USER
# -----------------------------
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        logger.warning(f"Registration failed - Email already exists: {user.email}")
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(f"New user registered: {user.email} as {user.role}")

    return {"message": "User registered successfully"}


# -----------------------------
# LOGIN USER (OAuth2 Compatible)
# -----------------------------
@router.post("/login", response_model=schemas.TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()

    if not user:
        logger.warning(f"Login failed - User not found: {form_data.username}")
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(form_data.password, user.password):
        logger.warning(f"Login failed - Wrong password for: {form_data.username}")
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": user.email}
    )

    logger.info(f"User logged in successfully: {user.email}")

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
