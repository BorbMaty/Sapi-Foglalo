from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    # username: str
    name: str
    email: str
    
    class Config:
        orm_mode = True

class UserWithPasswordResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True