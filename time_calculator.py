import re 
def add_time(start_time, duration, start_day=None):
    # Extract the hour, minutes, and period (AM/PM) from the start time
    start_hour, start_minutes, period = re.split(r":| ", start_time)

    # Extract the duration hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Convert the start hour to 24-hour clock format
    start_hour = int(start_hour) % 12
    if period.lower() == "pm":
        start_hour += 12

    # Calculate the total minutes of the start time and duration
    total_minutes = (start_hour * 60) + int(start_minutes) + (duration_hours * 60) + duration_minutes

    # Calculate the new hour and minutes
    new_hour = (total_minutes // 60) % 24
    new_minutes = total_minutes % 60

    # Determine the new period (AM/PM)
    new_period = "AM" if new_hour < 12 else "PM"

    # Convert the new hour to 12-hour clock format
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12

    # Calculate the number of days later
    days_later = total_minutes // (24 * 60)

    # Get the day of the week if provided
    if start_day:
        start_day = start_day.capitalize()
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time = f"{new_hour:02d}:{new_minutes:02d} {new_period}, {new_day}"
    else:
        new_time = f"{new_hour:02d}:{new_minutes:02d} {new_period}"

    # Add "next day" or "(n days later)" if applicable
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
