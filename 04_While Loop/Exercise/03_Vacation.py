cash_for_trip = float(input())
cash_saved = float(input())

days = 0
spending_frenzy = 0
while cash_saved != cash_for_trip and spending_frenzy != 5:
    type_of_action = input()  # "spend" или "save";
    amount = float(input())
    if type_of_action == "save":
        cash_saved += amount
        spending_frenzy = 0
    elif type_of_action == "spend":
        cash_saved -= amount
        spending_frenzy += 1
        if cash_saved < 0:
            cash_saved = 0
    days += 1

if spending_frenzy == 5:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
