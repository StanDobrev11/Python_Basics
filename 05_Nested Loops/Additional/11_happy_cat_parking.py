days = int(input())
hours_stay = int(input())


total_cost = 0
for day in range(1, days + 1):
    daily_cost = 0
    for hour in range(1, hours_stay + 1):
        if day % 2 == 0 and hour % 2 == 1:
            hour_cost = 2.50
        elif day % 2 == 1 and hour % 2 == 0:
            hour_cost = 1.25
        else:
            hour_cost = 1
        daily_cost += hour_cost
    total_cost += daily_cost
    print(f"Day: {day} - {daily_cost:.2f} leva")
print(f"Total: {total_cost:.2f} leva")
