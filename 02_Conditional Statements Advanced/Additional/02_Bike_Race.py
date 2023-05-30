juniors = (5.50, 8, 12.25, 20)
seniors = (7, 9.50, 13.75, 21.50)
EXPENSES = 5

type_of_race = {"trail": 0, "cross-country": 1, "downhill": 2, "road": 3}

junior_riders = int(input())
senior_riders = int(input())
race_type = input()

race = type_of_race[race_type]

sum_donated = junior_riders * juniors[race] + senior_riders * seniors[race]

if race_type == "cross-country" and (junior_riders + senior_riders >= 50):
    sum_donated *= (1 - 0.25)

sum_donated *= (100 - EXPENSES) / 100

print(f"{sum_donated:.2f}")
