def add_time(start, duration, day_of_the_week):
    list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = [0, 1, 2, 3, 4, 5, 6]
    d_week = dict(zip(list_of_days, day_index))
    future_day = [key for key, value in d_week.items() if key == day_of_the_week]
    pm_am = start.split()[1]

    time_start = start.split(":")
    time_start_hrs = int(time_start[0])
    time_start_min = int(time_start[1].strip("PAM"))

    time_duration = duration.split(":")
    time_duration_hrs = int(time_duration[0])
    time_duration_min = int(time_duration[1])

    new_hrs = time_start_hrs + time_duration_hrs
    new_min = time_start_min + time_duration_min
    new_hrs_min = new_hrs + new_min
    num_day = time_duration_hrs // 24

    while "AM" in start:
        if new_hrs or new_hrs_min >= 12:
            new_hrs = new_hrs % 12
            pm_am = pm_am.replace("AM", "PM")
        else:
            new_hrs = new_hrs

        if new_min >= 60:
            new_hrs += 1
            new_min = new_min % 60
        else:
            new_min = new_min

        if len(str(new_min)) == 1:
            new_min = "0" + str(new_min)

        break

    while "PM" in start:
        if time_start_hrs + (time_duration_hrs % 12) >= 12:
            num_day += 1
            n = (d_week.get(day_of_the_week) + num_day)
            future_day = [key for key, value in d_week.items() if value == n]
        else:
            new_hrs = new_hrs

        if new_hrs or new_hrs_min >= 12:
            new_hrs = new_hrs % 12
            pm_am = pm_am.replace("PM", "AM")
        else:
            new_hrs = new_hrs

        if new_min >= 60:
            new_hrs += 1
            new_min = new_min % 60
        else:
            new_min = new_min

        if len(str(new_min)) == 1:
            new_min = "0" + str(new_min)

        break

    future_day = "".join(future_day)
    new_time = f"{new_hrs}:{new_min} {pm_am}, {future_day}"

    return new_time


print(add_time("3:00 PM", "3:10", "Monday"))
print(add_time("11:30 AM", "2:32", "Tuesday"))
print(add_time("11:43 AM", "00:20", "Wednesday"))
print(add_time("6:30 PM", "6:01", "Thursday"))
print(add_time("10:10 PM", "3:30", "Saturday"))
