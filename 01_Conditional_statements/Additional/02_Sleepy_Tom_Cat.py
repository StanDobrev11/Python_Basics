PLAY_TIME = 30000
YEAR = 365  # days

rest_days = int(input())

PLAY_TIME_WORK = 63  # minutes
PLAY_TIME_NO_WORK = 127  # minutes

days_at_work = YEAR - rest_days

play_no_work = rest_days * PLAY_TIME_NO_WORK
play_work = days_at_work * PLAY_TIME_WORK

norm = PLAY_TIME - play_work - play_no_work
norm_hours = abs(norm) // 60
norm_mins = abs(norm) % 60

if norm < 0:
    print("Tom will run away")
    print(f"{norm_hours} hours and {norm_mins} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{norm_hours} hours and {norm_mins} minutes less for play")
