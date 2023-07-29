# modules/previous_week_dates.py

import datetime

def get_previous_week_dates(user_date):
    try:
        # Calculate the start and end dates of the previous week.
        start_of_week = user_date - datetime.timedelta(days=user_date.weekday() + 7)
        end_of_week = user_date - datetime.timedelta(days=user_date.weekday() + 1)

        # Generate a list of dates for the previous week in the format ddmmyyyy.
        previous_week_dates = [date_obj.strftime("%d%m%Y") for date_obj in [start_of_week + datetime.timedelta(days=i) for i in range(7)]]

        return previous_week_dates
    except ValueError:
        print("Invalid date format. Please enter a valid date in the format ddmmyyyy.")
        return None
