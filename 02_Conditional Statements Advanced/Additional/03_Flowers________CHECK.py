spring_summer_flower_prices = [2, 4.1, 2.5]
autumn_winter_flower_prices = [3.75, 4.5, 4.15]
ARRANGEMENT = 2

chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

is_holiday = True
if holiday == 'N':
    is_holiday = False

is_autumn_winter = False
if season == "Winter" or season == "Autumn":
    is_autumn_winter = True

if is_autumn_winter:
    cost = chrysanthemum * autumn_winter_flower_prices[0]\
           + roses * autumn_winter_flower_prices[1]\
           + tulips * autumn_winter_flower_prices[2]
else:
    cost = chrysanthemum * spring_summer_flower_prices[0]\
           + roses * spring_summer_flower_prices[1]\
           + tulips * spring_summer_flower_prices[2]

if is_holiday:
    cost *= (100 + 15) / 100

if not is_autumn_winter:
    if tulips > 7:
        cost *= (100 - 5) / 100
if is_autumn_winter:
    if roses >= 10:
        cost *= (100 - 10) / 100
if tulips + roses + chrysanthemum > 20:
    cost *= (100 - 20) / 100

total_cost = cost + ARRANGEMENT
print(f"{total_cost:.2f}")
