def add_time(start, duration, day=""):
  time_ampm = start.split()          # start time in list format [hr:min, AM/PM]
  start_time = time_ampm[0].split(":")    # start time as list [hr, min]
  dur_time = duration.split(":")      # duration as list [hr, min]
  new_hr = 0
  new_ampm = " "
  days_later = 0
  count = 0

  days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  # make a circular list (from suggestion by Lante Dellarovere: https://stackoverflow.com/questions/56106817/how-to-turn-a-list-into-a-circular-list-in-python-3)
  for _ in range(len(days_of_week)):
    x = days_of_week.pop(0)
    days_of_week.append(x)

  new_min = int(start_time[1]) + int(dur_time[1])
  if new_min > 60:              
    new_min -= 60
    new_hr += 1          # increase hr by 1 if total mins exceeds 60
    
  new_hr += int(start_time[0]) + int(dur_time[0]) 

  if new_hr < 12:  #if hr < 12, AM/PM stays the same
    new_ampm = time_ampm[1]
  else:            #if hr >= 12, count how many 12 hour periods have passed
    while new_hr > 12:
      new_hr -= 12
      count += 1
    days_later = (count//2) 
    if (count % 2) == 1 or new_hr == 12:  #if count is odd, change AM/PM
      if time_ampm[1] == 'AM':
        new_ampm = 'PM'
      else:
        new_ampm = 'AM'
        days_later += 1  #add extra day if going from PM to AM
    else:              #if count is even, AM/PM stays the same
      new_ampm = time_ampm[1]
        
      
  new_time = f'{new_hr}:{"{:02d}".format(new_min)} {new_ampm}'

  if day:                  # only display if passed as arg
    if days_later == 0:
      new_time += f', {day.title()}'    # same day
    else:
      ind_start_day = days_of_week.index(day.title())    # find index of start day
      ind_to_day = (ind_start_day + days_later) % 7      # find index of end day
      new_day = days_of_week[ind_to_day]        # convert to day name
      new_time += f', {new_day}'
  if not days_later == 0:
    if days_later == 1:
      new_time += ' (next day)'
    else:
      new_time += f' ({days_later} days later)'
  
  return new_time