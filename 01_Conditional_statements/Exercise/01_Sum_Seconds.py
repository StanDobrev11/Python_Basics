time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time_seconds = time_first + time_second + time_third
time_minutes = total_time_seconds // 60
time_seconds = total_time_seconds % 60

if time_seconds < 10:
    print(f"{time_minutes}:0{time_seconds}")
else:
    print(f"{time_minutes}:{time_seconds}")
    print(f"{time_minutes}:{time_seconds:02d}")
