DISCOUNT_THRONES = 50 / 100
DISCOUNT_LUCIFER = 40 / 100
DISCOUNT_PROTECTOR = 30 / 100
DISCOUNT_TOTALDRAMA = 20 / 100
DISCOUNT_AREA = 10 / 100

budget = float(input())
series_count = int(input())

total_amount = 0
for series in range(series_count):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        series_price *= (1 - DISCOUNT_THRONES)
    elif series_name == "Lucifer":
        series_price *= (1 - DISCOUNT_LUCIFER)
    elif series_name == "Protector":
        series_price *= (1 - DISCOUNT_PROTECTOR)
    elif series_name == "TotalDrama":
        series_price *= (1 - DISCOUNT_TOTALDRAMA)
    elif series_name == "Area":
        series_price *= (1 - DISCOUNT_AREA)

    total_amount += series_price

if budget >= total_amount:
    cash_left = budget - total_amount
    print(f"You bought all the series and left with {cash_left:.2f} lv.")
else:
    cash_needed = total_amount - budget
    print(f"You need {cash_needed:.2f} lv. more to buy the series!")
