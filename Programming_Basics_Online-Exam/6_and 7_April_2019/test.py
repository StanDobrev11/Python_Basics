from math import ceil

series_name = str(input())
series_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
relax_time = break_length / 4

time_needed = relax_time + lunch_time + series_length
free_time = break_length - time_needed

if time_needed <= break_length:
    print(f"You have enough time to watch {series_name} and left with {ceil(free_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(-free_time)} more minutes.")