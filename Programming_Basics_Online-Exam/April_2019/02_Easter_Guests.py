import math

EASTER_BREAD_PRICE = 4.00
EGG_PRICE = 0.45

guest_count = int(input())
budget = int(input())


easter_bread_needed = math.ceil(guest_count / 3)
eggs_needed = guest_count * 2

total_price = easter_bread_needed * EASTER_BREAD_PRICE + eggs_needed * EGG_PRICE

cash_left = budget - total_price

if cash_left >= 0:
  print(f"Lyubo bought {easter_bread_needed} Easter bread and {eggs_needed} eggs.")
  print(f"He has {cash_left:.2f} lv. left.")
else:
  cash_needed = cash_left * -1
  print(f"Lyubo doesn't have enough money.")
  print(f"He needs {cash_needed:.2f} lv. more.")