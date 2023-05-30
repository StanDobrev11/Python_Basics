from math import ceil

FLOWER_1_PRICE = 3.25
FLOWER_2_PRICE = 4
FLOWER_3_PRICE = 3.5
FLOWER_4_PRICE = 8
TAXES = 0.05

flower_1_qtity = int(input())
flower_2_qtity = int(input())
flower_3_qtity = int(input())
flower_4_qtity = int(input())
gift_price = float(input())

profit = flower_1_qtity * FLOWER_1_PRICE + \
         flower_2_qtity * FLOWER_2_PRICE + \
         flower_3_qtity * FLOWER_3_PRICE + \
         flower_4_qtity * FLOWER_4_PRICE
profit_after_tax = profit * (1 - TAXES)

remaining_cash = abs(profit_after_tax - gift_price)
if profit_after_tax >= gift_price:
    print(f"She is left with {int(remaining_cash)} leva.")
else:
    print(f"She will have to borrow {ceil(remaining_cash)} leva.")
