budget = float(input())
season = input()

SUMMER_PRICE_BULGARIA = 0.3
SUMMER_PRICE_BALKANS = 0.4
WINTER_PRICE_BULGARIA = 0.7
WINTER_PRICE_BALKANS = 0.8
EUROPE_PRICE = 0.9

destination = ""
costs = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        costs = budget * SUMMER_PRICE_BULGARIA
        season = "Camp"
    else:
        costs = budget * WINTER_PRICE_BULGARIA
        season = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        costs = budget * SUMMER_PRICE_BALKANS
        season = "Camp"
    else:
        costs = budget * WINTER_PRICE_BALKANS
        season = "Hotel"
else:
    destination = "Europe"
    costs = budget * EUROPE_PRICE
    season = "Hotel"

print(f"Somewhere in {destination}")
print(f"{season} - {costs:.2f}")
