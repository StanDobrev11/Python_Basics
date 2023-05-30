current_record = float(input())
distance = float(input())
time_per_meter = float(input())


slow_down_seconds = 12.5 * int(distance / 15)
time = distance * time_per_meter + slow_down_seconds

if time < current_record:
    print(f" Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(current_record - time):.2f} seconds slower.")
