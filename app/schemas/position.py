# schemas/position.py
from pydantic import BaseModel

class PositionCreate(BaseModel):
    name: str

class PositionResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Replace orm_mode with from_attributes for Pydantic v2
