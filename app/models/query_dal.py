from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from app.models.reserve import Reserve
from app.models.user import User

class QueryDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

async def get_reservations_for_room_and_date(self, room_id: int, date: str):
    """
    Fetch all reservations for a specific room on a specific date.

    Args:
        room_id (int): The ID of the room.
        date (str): The date for which to fetch reservations.

    Returns:
        List[dict]: Reservations in the required format.
    """
    from datetime import datetime
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()

    query = (
        select(
            Reserve.id.label("ReserveId"),
            User.name.label("user_name"),
            Reserve.room_id.label("RoomId"),
            Reserve.date.label("Date"),
            Reserve.start_hour.label("StartHour"),
            Reserve.end_hour.label("EndHour"),
        )
        .join(User, Reserve.user_id == User.id)
        .where(
            and_(
                Reserve.room_id == room_id,
                Reserve.date == date_obj
            )
        )
    )
    result = await self.db_session.execute(query)
    rows = result.mappings().all()

    # Format the result
    return [
        {
            "ReserveId": row["ReserveId"],
            "user_name": row["user_name"],
            "RoomId": row["RoomId"],
            "Date": row["Date"].strftime("%Y-%m-%d"),
            "StartHour": row["StartHour"].strftime("%H:%M:%S"),
            "EndHour": row["EndHour"].strftime("%H:%M:%S"),
        }
        for row in rows
    ]

