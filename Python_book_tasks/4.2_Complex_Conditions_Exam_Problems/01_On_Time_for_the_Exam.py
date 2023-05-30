hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

time_of_exam = (hour_of_exam * 60) + minutes_of_exam
time_of_arrival = (hour_of_arrival * 60) + minute_of_arrival

time_difference_in_minutes = time_of_arrival - time_of_exam

late = "Late"
on_time = "On time"
early = "Early"

student_arrival = late
if time_difference_in_minutes < -30:
    student_arrival = early
elif time_difference_in_minutes <= 0:
    student_arrival = on_time

result = ""
if time_difference_in_minutes != 0:
    hours_difference = abs(time_difference_in_minutes) // 60
    minutes_difference = abs(time_difference_in_minutes) % 60
    if hours_difference > 0:
        result = f"{hours_difference}:{minutes_difference:02} hours"
    else:
        result = f"{minutes_difference} minutes"

    if time_difference_in_minutes < 0:
        result += "before the start"
    else:
        result += "after the start"

print(student_arrival)
if result:
    print(result)

# time_of_exam = minutes_of_exam / 60 + hour_of_exam
# time_of_arrival = minute_of_arrival / 60 + hour_of_arrival
#
# late = 0
# if time_of_arrival > time_of_exam:
#     late = (time_of_arrival - time_of_exam)
#     if late < 1:
#         late = round(late * 60)
#         print(f"Late {late} minutes after the start")
#     else:
#         hh = int(late)
#         mm = round((late - hh) * 60)
#         print(f"Late {hh}:{mm:02d} hours after the start")
#
# elif (time_of_exam - 0.5) <= time_of_arrival <= time_of_exam:
#     on_time = time_of_exam - time_of_arrival
#     if on_time == 0:
#         print(f"On time")
#     else:
#         mm = round(on_time * 60)
#         print(f"On time {mm}  minutes before the start")
#
# else:
#     early = time_of_exam - time_of_arrival
#     if early < 1:
#         early = round(early * 60)
#         print(f"Early {early} minutes before the start")
#     else:
#         hh = int(early)
#         mm = round((early - hh) * 60)
#         print(f"Early {hh}:{mm:02d} hours before the start")
