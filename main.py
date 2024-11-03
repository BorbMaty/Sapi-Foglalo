import app.database  # Ensure Firebase is initialized
from app.models.reserve import ReserveDAL
from datetime import date, time

def main():
    try:
        # Initialize ReserveDAL and create a reservation
        reserve_dal = ReserveDAL()
        user_id = 1
        room_id = 230
        reserve_date = date(2024, 10, 31)
        start_hour = time(9, 0)
        end_hour = time(11, 0)

        new_reserve_id = reserve_dal.create_reserve(user_id, room_id, reserve_date, start_hour, end_hour)
        print(f"Created new reserve with ID: {new_reserve_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
