budget = float(input())
season = input()

car_class = ""
car = ""
cost = 0
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        cost = budget * 35 / 100
    elif season == "Winter":
        car = "Jeep"
        cost = budget * 65 / 100
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        cost = budget * 45 / 100
    elif season == "Winter":
        car = "Jeep"
        cost = budget * 80 / 100
elif budget > 500:
    car_class = "Luxury class"
    car = "Jeep"
    cost = budget * 90 / 100

print(f"{car_class}\n"
      f"{car} - {cost:.2f}")
