# schemas/position.py
from pydantic import BaseModel

class PositionCreate(BaseModel):
    name: str

class PositionResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
