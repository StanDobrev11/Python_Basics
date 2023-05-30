days = int(input())
hours_parked = int(input())

total = 0
for each_day in range(1, days + 1):
    paid_per_day = 0
    for each_hour in range(1, hours_parked + 1):
        if each_day % 2 == 0 and each_hour % 2 == 1:
            parking_fare = 2.5
        elif each_day % 2 == 1 and each_hour % 2 == 0:
            parking_fare = 1.25
        else:
            parking_fare = 1

        paid_per_day += parking_fare
        total += parking_fare
    print(f"Day: {each_day} - {paid_per_day:.2f} leva")

print(f"Total: {total:.2f} leva")
