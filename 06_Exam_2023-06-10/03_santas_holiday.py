days_of_stay = int(input())
accommodation_type = input()  # "room for one person", "apartment" или "president apartment"
rate = input()  # "positive" или "negative"

room_for_one_person = 18
apartment = 25
president_apartment = 35

apartment_discount_to_10_days = 0.3
apartment_discount_to_15_days = 0.35
apartment_discount_more_than_15_days = 0.5

president_apartment_discount_to_10_days = 0.1
president_apartment_discount_to_15_days = 0.15
president_apartment_discount_more_than_15_days = 0.2

discount_if_positive = 1 + 0.25
discount_if_negative = 1 - 0.1

nights_stay = days_of_stay - 1
cost = 0
if accommodation_type == "room for one person":
    cost = nights_stay * room_for_one_person
elif accommodation_type == "apartment":
    if days_of_stay <= 10:
        cost = nights_stay * apartment * (1 - apartment_discount_to_10_days)
    elif days_of_stay <= 15:
        cost = nights_stay * apartment * (1 - apartment_discount_to_15_days)
    else:
        cost = nights_stay * apartment * (1 - apartment_discount_more_than_15_days)
elif accommodation_type == "president apartment":
    if days_of_stay <= 10:
        cost = nights_stay * president_apartment * (1 - president_apartment_discount_to_10_days)
    elif days_of_stay <= 15:
        cost = nights_stay * president_apartment * (1 - president_apartment_discount_to_15_days)
    else:
        cost = nights_stay * president_apartment * (1 - president_apartment_discount_more_than_15_days)

if rate == "positive":
    ttl_cost = cost * discount_if_positive
else:
    ttl_cost = cost * discount_if_negative

print(f"{ttl_cost:.2f}")
