initial_amount = float(input())
sex = input()
age = int(input())
discipline = input()

subscription_card = 0
if sex == "m":
    if discipline == "Gym":
        subscription_card = 42
    elif discipline == "Boxing":
        subscription_card = 41
    elif discipline == "Yoga":
        subscription_card = 45
    elif discipline == "Zumba":
        subscription_card = 34
    elif discipline == "Dances":
        subscription_card = 51
    elif discipline == "Pilates":
        subscription_card = 39
else:
    if discipline == "Gym":
        subscription_card = 35
    elif discipline == "Boxing":
        subscription_card = 37
    elif discipline == "Yoga":
        subscription_card = 42
    elif discipline == "Zumba":
        subscription_card = 31
    elif discipline == "Dances":
        subscription_card = 53
    elif discipline == "Pilates":
        subscription_card = 37

if age <= 19:
    subscription_card -= 0.2 * subscription_card

money_needed = abs(initial_amount - subscription_card)
if subscription_card <= initial_amount:
    print(f"You purchased a 1 month pass for {discipline}.")
else:
    print(f"You don't have enough money! You need ${money_needed:.2f} more.")
