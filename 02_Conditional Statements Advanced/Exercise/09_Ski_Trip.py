ROOM = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

apartment_discount = {"less_than_10": 30, "less_than_15": 35, "more_than_15": 50}
president_apartment_discount = {"less_than_10": 10, "less_than_15": 15, "more_than_15": 20}

days_stay = int(input())
type_of_accommodation = input()
score_of_the_stay = input()

nights = days_stay - 1

nights_stay = ""
if nights < 10:
    nights_stay = "less_than_10"
elif nights < 15:
    nights_stay = "less_than_15"
elif nights >= 15:
    nights_stay = "more_than_15"

room_cost = ROOM * nights
apartment_cost = APARTMENT * nights * (100 - apartment_discount[nights_stay]) / 100
president_apartment_cost = PRESIDENT_APARTMENT * nights * (100 - president_apartment_discount[nights_stay]) / 100

total_cost = 0
if type_of_accommodation == "room for one person":
    if score_of_the_stay == "positive":
        total_cost = room_cost * (100 + 25) / 100
    else:
        total_cost = room_cost * (100 - 10) / 100
elif type_of_accommodation == "apartment":
    if score_of_the_stay == "positive":
        total_cost = apartment_cost * (100 + 25) / 100
    else:
        total_cost = apartment_cost * (100 - 10) / 100
elif type_of_accommodation == "president apartment":
    if score_of_the_stay == "positive":
        total_cost = president_apartment_cost * (100 + 25) / 100
    else:
        total_cost = president_apartment_cost * (100 - 10) / 100

print(f"{total_cost:.2f}")
