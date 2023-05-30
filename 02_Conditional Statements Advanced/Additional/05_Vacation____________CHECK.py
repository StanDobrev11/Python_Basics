budget = float(input())
season = input()

type_of_accommodation = ""
destination = ""
cost = 0
if budget <= 1000:
    type_of_accommodation = "Camp"
    if season == "Summer":
        destination = "Alaska"
        cost = budget * 65 / 100
    elif season == "Winter":
        destination = "Morocco"
        cost = budget * 45 / 100
elif budget <= 3000:
    type_of_accommodation = "Hut"
    if season == "Summer":
        destination = "Alaska"
        cost = budget * 80 / 100
    elif season == "Winter":
        destination = "Morocco"
        cost = budget * 60 / 100
elif budget > 3000:
    type_of_accommodation = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        cost = budget * 90 / 100
    elif season == "Winter":
        destination = "Morocco"
        cost = budget * 90 / 100

print(f"{destination} - {type_of_accommodation} - {cost:.2f}")
