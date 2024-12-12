from fastapi import APIRouter, HTTPException, Depends, status
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
async def login(
    login_request: LoginRequest,
    user_dal: UserDAL = Depends(get_user_dal),
    password_dal: PasswordDAL = Depends(get_password_dal),
):
    try:
        print(f"Login attempt for email: {login_request.email}")
        
        # Fetch the user by email
        user = user_dal.get_user_by_email(login_request.email)
        if not user:
            print(f"User with email {login_request.email} not found.")
            raise HTTPException(status_code=404, detail="User not found")

        print(f"User found: ID = {user.id}, Name = {user.name}")

        # Verify password
        if not password_dal.verify_password(user.id, login_request.password):
            print(f"Incorrect password for user ID = {user.id}")
            raise HTTPException(status_code=401, detail="Incorrect password")

        print(f"User {user.id} logged in successfully.")
        return user

    except Exception as e:
        print(f"Unexpected error during login: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {e}"
        )

@password_router.get("/users-with-passwords", response_model=list[UserWithPasswordResponse])
async def get_users_with_passwords(db: Session = Depends(get_db)):
    """
    Retrieves all users along with their associated passwords by performing
    a JOIN between Users and Passwords tables.
    """
    try:
        results = (
        db.query(User, Password.password)
        .join(Password, User.id == Password.userId)
        .all()
    )

        users_with_passwords = [
        UserWithPasswordResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            password=password  # Now this is the `password` string, not the object
        )
        for user, password in results
    ]
        return users_with_passwords
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database query failed") from e
