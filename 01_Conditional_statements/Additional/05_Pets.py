from math import ceil

days_away = int(input())
food_left_while_away = int(input())

dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())  # in grams

animals_eat = (dog_food_per_day + cat_food_per_day + turtle_food_per_day / 1000) * days_away

food_remaining = 0
if food_left_while_away >= animals_eat:
    food_remaining = food_left_while_away - animals_eat
    print(f"{int(food_remaining)}  kilos of food left.")
else:
    food_remaining = animals_eat - food_left_while_away
    print(f"{ceil(food_remaining)} more kilos of food are needed.")
