# app/api/users_router.py
from fastapi import APIRouter, HTTPException, Depends
from app.schemas import UserCreate, UserResponse
from app.database import get_db
from app.models.user import UserDAL

users_router = APIRouter()

def get_user_dal(db=Depends(get_db)):
    return UserDAL(db)

@users_router.get("/", response_model=list[UserResponse])
async def get_users(user_dal: UserDAL = Depends(get_user_dal)):
    return user_dal.get_all_users()

@users_router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, user_dal: UserDAL = Depends(get_user_dal)):
    user = user_dal.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@users_router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, user_dal: UserDAL = Depends(get_user_dal)):
    # Check if a user with the same email already exists
    existing_user = user_dal.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    return user_dal.create_user(
        name=user.name,
        email=user.email,
        PositionId=user.PositionId,
        year=user.year
    )
    return user_dal.create_user(user)

@users_router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, user_dal: UserDAL = Depends(get_user_dal)):
    updated_user = user_dal.update_user(
        user_id=user_id,
        name=user.name,
        email=user.email,
        PositionId=user.PositionId,
        year=user.year
    )
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@users_router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int, user_dal: UserDAL = Depends(get_user_dal)):
    user_deleted = user_dal.delete_user(user_id)
    if not user_deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}


@users_router.get("/user-id/{name}")
def get_user_id(name: str,  user_dal: UserDAL = Depends(get_user_dal)):
    user_id = user_dal.get_id_by_name(name)
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}
