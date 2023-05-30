group_budget = int(input())
season = input()
fishing_party = int(input())

boat_rent = {"Spring": 3000, "Summer": 4200, "Autumn": 4200, "Winter": 2600}
group_discount = {"to_6": 10, "to_11": 15, "over_11": 25}
DISCOUNT_IF_EVEN_COUNT = 5  # except if autumn

group = ""
if fishing_party > 11:
    group = "over_11"
elif fishing_party > 6:
    group = "to_11"
elif fishing_party >= 1:
    group = "to_6"
total_cost = boat_rent[season] * (100 - group_discount[group]) / 100

if fishing_party % 2 == 0:
    if season == "Autumn":
        pass
    else:
        total_cost = total_cost * (100 - DISCOUNT_IF_EVEN_COUNT) / 100

if total_cost <= group_budget:
    remaining_cash = group_budget - total_cost
    print(f"Yes! You have {remaining_cash:.2f} leva left.")
else:
    cash_needed = total_cost - group_budget
    print(f"Not enough money! You need {cash_needed:.2f} leva.")
