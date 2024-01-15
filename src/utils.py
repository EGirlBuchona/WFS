# src/utils.py
from datetime import datetime, timedelta

def get_day_name(offset):
    # Return the day name for a specific offset from today
    date = datetime.now() + timedelta(days=offset)
    return date.strftime("%A")  # e.g., "Monday", "Tuesday", etc.
