# modules/user_input_date.py

import datetime

def get_user_input_date(user_input):
    try:
        # Convert the user input to a datetime object.
        date_obj = datetime.datetime.strptime(user_input, "%d%m%Y")
        return date_obj  # Return the datetime object directly
    except ValueError:
        print("Invalid date format. Please enter a valid date in the format ddmmyyyy.")
        return None
