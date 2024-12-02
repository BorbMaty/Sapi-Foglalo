# app/api/users_router.py


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError  # Fix: Import SQLAlchemyError
from app.schemas import UserWithPasswordResponse
from app.database import get_db
from app.models.user import User, UserDAL  # Fix: Import User model
from app.models.passwords import Password, PasswordDAL  # Fix: Import Password model
from app.schemas import UserResponse
from app.schemas.password import LoginRequest


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

@password_router.get("/users-with-passwords", response_model=list[UserWithPasswordResponse])
async def get_users_with_passwords(db: Session = Depends(get_db)):
    """
    Retrieves all users along with their associated passwords by performing
    a JOIN between Users and Passwords tables.
    """
    try:
        # Perform the join query
        results = (
            db.query(User, Password)
            .join(Password, User.id == Password.userId)
            .all()
        )

        # Map results into a structured response
        users_with_passwords = [
            UserWithPasswordResponse(
                id=user.id,
                name=user.name,
                email=user.email,
                password=password
            )
            for user, password in results
        ]

        return users_with_passwords
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database query failed") from e
