# app/api/users_router.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import UserResponse, LoginRequest
from app.database import get_db
from app.models.user import UserDAL
from app.models.passwords import PasswordDAL, Password

password_router = APIRouter()

def get_user_dal(db: Session = Depends(get_db)):
    return UserDAL(db)

def get_password_dal(db: Session = Depends(get_db)):
    return PasswordDAL(db)

@password_router.post("/login", response_model=UserResponse)
async def login(login_request: LoginRequest, user_dal: UserDAL = Depends(get_user_dal), password_dal: PasswordDAL = Depends(get_password_dal)):
    # Get the user by email
    user = user_dal.get_user_by_email(login_request.email)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the password
    if not password_dal.verify_password(user.id, login_request.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    # If login is successful, return the user details
    return user
