def add_time(start_time, duration, start_day=None):
  start_time, period = start_time.split()
  start_hour, start_minute = map(int, start_time.split(':'))
  start_hour = start_hour % 12

  duration_hour, duration_minute = map(int, duration.split(':'))

  total_minutes = start_hour * 60 + start_minute
  total_minutes += duration_hour * 60 + duration_minute

  new_hour = (total_minutes // 60) % 24
  new_minute = total_minutes % 60

  new_period = period
  if new_hour >= 12:
    new_period = "PM" if period == "AM" else "AM"

  new_hour = new_hour % 12
  if new_hour == 0:
    new_hour = 12

  new_time = f"{new_hour:02d}:{new_minute:02d} {new_period}"

  if start_day:
    start_day = start_day.lower().capitalize()
    day_mapping = {
      "Monday": 0,
      "Tuesday": 1,
      "Wednesday": 2,
      "Thursday": 3,
      "Friday": 4,
      "Saturday": 5,
      "Sunday": 6
    }
    start_day_index = day_mapping[start_day]

    new_day_index = (start_day_index + total_minutes // (24 * 60)) % 7
    new_day = list(day_mapping.keys())[list(
      day_mapping.values()).index(new_day_index)]
    new_time += f", {new_day}"

  days_later = total_minutes // (24 * 60)
  remaining_minutes = total_minutes % (24 * 60)

  if days_later == 1:
    new_time += " (next day)"
  elif days_later > 1:
    new_time += f" ({days_later} days later)"

  if remaining_minutes < 10:
    remaining_minutes = f"0{remaining_minutes}"

  new_time = new_time.replace(":00", f":{remaining_minutes}")

  return new_time
