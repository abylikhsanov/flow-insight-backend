from datetime import timedelta
from datetime import datetime
from mockseries.utils import datetime_range
from mockseries.trend import LinearTrend
from mockseries.seasonality import SinusoidalSeasonality
from mockseries.noise import RedNoise

async def fetch_time_series(item_id: int,
                          start_year: int,
                          start_month: int,
                          start_day: int,
                          end_year: int,
                          end_month: int,
                          end_day: int):
    trend = LinearTrend(coefficient=2, time_unit=timedelta(days=4), flat_base=100)
    seasonality = SinusoidalSeasonality(amplitude=20, period=timedelta(days=7)) \
        + SinusoidalSeasonality(amplitude=4, period=timedelta(days=1))
    noise = RedNoise(mean=0, std=3, correlation=0.5)
    timeseries = trend + seasonality + noise
    time_points = datetime_range(
        granularity=timedelta(hours=1),
        start_time=datetime(start_year, start_month, start_day),
        end_time=datetime(end_year, end_month, end_day),
    )
    ts_values = timeseries.generate(time_points=time_points)
    print("TimeSeries length", len(ts_values))

    number_of_days = (datetime(end_year, end_month, end_day) - datetime(start_year, start_month, start_day)).days

    # Prepare the result list
    result = []

    # Iterate over each day to get the daily value
    for day_index in range(number_of_days):
        # Calculate the daily average by summing 24-hour data points
        start_index = day_index * 24  # Starting index for each day's data points
        end_index = start_index + 24  # Ending index for each day's data points
        daily_average = sum(ts_values[start_index:end_index]) / 24

        # Construct the date in the required format
        date = datetime(start_year, start_month, start_day) + timedelta(days=day_index)
        formatted_date = date.strftime("%-m/%-d/%Y")  # Format date as M/D/YYYY

        # Append the formatted date and daily average to the result list
        result.append([formatted_date, daily_average])

    # Print the generated time series length for verification
    print("Generated TimeSeries length:", result)
    return result