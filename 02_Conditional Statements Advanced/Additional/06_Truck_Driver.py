season = input()
kilometers_per_month = float(input())

taxes = 0.1
is_spring_autumn = False
is_summer = False
is_winter = False

if season == "Spring" or season == "Autumn":
    is_spring_autumn = True
elif season == "Winter":
    is_winter = True
elif season == "Summer":
    is_summer = True

price_per_kilometer = 0
if is_spring_autumn:
    if kilometers_per_month <= 5000:
        price_per_kilometer = 0.75
    elif kilometers_per_month <= 10000:
        price_per_kilometer = 0.95
elif is_summer:
    if kilometers_per_month <= 5000:
        price_per_kilometer = 0.9
    elif kilometers_per_month <= 10000:
        price_per_kilometer = 1.1
elif is_winter:
    if kilometers_per_month <= 5000:
        price_per_kilometer = 1.05
    elif kilometers_per_month <= 10000:
        price_per_kilometer = 1.25

if 10000 < kilometers_per_month <= 20000:
    price_per_kilometer = 1.45

profit_per_season_after_tax = 4 * kilometers_per_month * price_per_kilometer * (1 - taxes)

print(f"{profit_per_season_after_tax:.2f}")
