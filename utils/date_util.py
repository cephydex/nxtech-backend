from datetime import datetime, timedelta
from pytz import timezone

def compareDates(date_str):
    tz = timezone('UTC')
    currentDate = datetime.now(tz)
    
    try:
        # Parse the provided date string into a datetime object
        target_dateTime = datetime.fromisoformat(date_str)
      
    except ValueError:
        # Handle the case where the date_str cannot be parsed
        return False
    
    time_diff = currentDate - target_dateTime

    time_threshold = timedelta(minutes=10)
  
    if time_diff > time_threshold:
        return True
    
    return False
