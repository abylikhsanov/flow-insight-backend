from fastapi import APIRouter
from app.sevices.mock_time_series import fetch_time_series

router = APIRouter()

@router.get("/{item_id}/{start_year}/{start_month}/{start_day}/{end_year}/{end_month}/{end_day}")
async def get_time_series(item_id: int,
                          start_year: int,
                          start_month: int,
                          start_day: int,
                          end_year: int,
                          end_month: int,
                          end_day: int):
    data = await fetch_time_series(item_id, start_year, start_month, start_day, end_year, end_month, end_day)
    return data