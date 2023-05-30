CALORIES_PER_MINUTE_WALKING = 5

minutes_per_walk = int(input())
walks_count_per_day = int(input())
calories_intake_per_day = int(input())

total_minutes_per_day = minutes_per_walk * walks_count_per_day
calories_burned = total_minutes_per_day * CALORIES_PER_MINUTE_WALKING

if calories_burned >= calories_intake_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
