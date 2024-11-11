# api/users_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import UserDAL, User
from app.schemas import UserCreate, UserResponse  # Import schemas
# app/api/users.py
from fastapi import APIRouter

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    return {"message": "Users endpoint"}


# Dependency to get a DAL instance
def get_user_dal(db: Session = Depends(get_db)):
    return UserDAL(db)

@users_router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, user_dal: UserDAL = Depends(get_user_dal)):
    return user_dal.create_user(name=user.name, email=user.email, PositionId=user.PositionId, year=user.year)

@users_router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, user_dal: UserDAL = Depends(get_user_dal)):
    db_user = user_dal.get_user_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@users_router.get("/users/", response_model=list[UserResponse])
def get_all_users(user_dal: UserDAL = Depends(get_user_dal)):
    return user_dal.get_all_users()

@users_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, user_dal: UserDAL = Depends(get_user_dal)):
    updated_user = user_dal.update_user(user_id, name=user.name, email=user.email, PositionId=user.PositionId, year=user.year)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@users_router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, user_dal: UserDAL = Depends(get_user_dal)):
    deleted_user = user_dal.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
