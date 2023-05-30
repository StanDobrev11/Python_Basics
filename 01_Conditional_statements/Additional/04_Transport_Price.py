# charge per kilometer
TAXI_INITIAL_CHARGE = 0.70
TAXI_DAY_FARE = 0.79
TAXI_NIGHT_FARE = 0.90
BUS_FARE = 0.09
TRAIN_FARE = 0.06

distance = int(input())
time_of_travel = input()

total_cost = 0
if distance < 20:
    if time_of_travel == "day":
        total_cost = TAXI_INITIAL_CHARGE + TAXI_DAY_FARE * distance
    else:
        total_cost = TAXI_INITIAL_CHARGE + TAXI_NIGHT_FARE * distance
elif distance < 100:
    total_cost = BUS_FARE * distance
else:
    total_cost = TRAIN_FARE * distance

print(f"{total_cost:.2f}")
