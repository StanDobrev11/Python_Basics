hours = int(input())
minutes = int(input())

ADD_TIME_MINUTES = 15

new_minutes = minutes + ADD_TIME_MINUTES
if new_minutes >= 60:
    new_minutes -= 60
    hours += 1
    if hours >= 24:
        hours = hours - 24

if new_minutes < 10:
    print(f"{hours}:0{new_minutes}")
else:
    print(f"{hours}:{new_minutes}")



