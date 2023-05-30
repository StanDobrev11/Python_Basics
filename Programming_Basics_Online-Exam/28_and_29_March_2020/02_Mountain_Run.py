record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter_in_seconds = float(input())

slowed_down = 0
if distance_in_meters >= 50:
    slowed_down = int(distance_in_meters / 50)

attempt_in_seconds = distance_in_meters * time_per_meter_in_seconds + slowed_down * 30
time_required = attempt_in_seconds - record_in_seconds

if attempt_in_seconds < record_in_seconds:
    print(f" Yes! The new record is {attempt_in_seconds:.2f} seconds.")
else:
    print(f"No! He was {time_required:.2f} seconds slower.")
