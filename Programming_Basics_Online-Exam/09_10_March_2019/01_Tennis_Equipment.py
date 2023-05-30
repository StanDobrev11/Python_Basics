from math import ceil

tennis_racket_price = float(input())
tennis_racket_pcs = int(input())
sneackers_sets = int(input())

sneackers_price = tennis_racket_price / 6

total_sum = tennis_racket_pcs * tennis_racket_price + sneackers_sets * sneackers_price
other_gear_price = total_sum * 0.2

by_player = int((total_sum + other_gear_price) / 8)
by_sponsors = ceil((total_sum + other_gear_price) * 7 / 8)

print(f"Price to be paid by Djokovic {by_player}")
print(f"Price to be paid by sponsors {by_sponsors}")
