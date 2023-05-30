season = input()
group_type = input()
group_qtity = int(input())
nights_stay = int(input())

if season == "Winter":
    season = 0
elif season == "Spring":
    season = 1
elif season == "Summer":
    season = 2

girls_sport = ["Gymnastics", "Athletics", "Volleyball"]
boys_sport = ["Judo", "Tennis", "Football"]
mixed_sport = ["Ski", "Cycling", "Swimming"]

girs_price_per_night = [9.60, 7.20, 15]
boys_price_per_night = [9.60, 7.20, 15]
mixed_price_per_night = [10, 9.50, 20]

if group_qtity >= 50:
    discount = 1 - 50 / 100
elif group_qtity >= 20:
    discount = 1 - 15 / 100
elif group_qtity >= 10:
    discount = 1 - 5 / 100
else:
    discount = 1

sport = ""
cost = 0
if group_type == "boys":
    sport = boys_sport[season]
    cost = boys_price_per_night[season] * group_qtity * nights_stay * discount

if group_type == "girls":
    sport = girls_sport[season]
    cost = girs_price_per_night[season] * group_qtity * nights_stay * discount

if group_type == "mixed":
    sport = mixed_sport[season]
    cost = mixed_price_per_night[season] * group_qtity * nights_stay * discount

print(f"{sport} {cost:.2f} lv.")
