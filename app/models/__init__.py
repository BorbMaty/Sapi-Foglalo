# app/models/__init__.py

from app.models.user import User
from app.models.position import Position,PositionDAL
from app.models.room import Room
from app.models.reserve import Reserve
from app.models.passwords import Password, PasswordDAL

# This ensures that SQLAlchemy knows about all models.
# You don’t need to import Base here because it's already in database.py
