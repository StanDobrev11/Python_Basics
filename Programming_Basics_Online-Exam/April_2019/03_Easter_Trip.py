destination = input()
dates = input()
days = int(input())

price_per_day = 0
if destination == "France":
    if dates == '21-23':
        price_per_day = 30
    elif dates == '24-27':
        price_per_day = 35
    else:
        price_per_day = 40

if destination == "Italy":
    if dates == '21-23':
        price_per_day = 28
    elif dates == '24-27':
        price_per_day = 32
    else:
        price_per_day = 39

if destination == "Germany":
    if dates == '21-23':
        price_per_day = 32
    elif dates == '24-27':
        price_per_day = 37
    else:
        price_per_day = 43

expenses = days * price_per_day

print(f"Easter trip to {destination} : {expenses:.2f} leva.")