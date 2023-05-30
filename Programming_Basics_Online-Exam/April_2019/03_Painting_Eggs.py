PRODUCTION_COST = 35 / 100  # 35% of total_price

egg_size = input().lower()
egg_color = input().lower()
count = int(input())

price_per_count = 0
if egg_size == 'large':
    if egg_color == 'red':
        price_per_count = 16
    elif egg_color == 'green':
        price_per_count = 12
    else:
        price_per_count = 9

if egg_size == 'medium':
    if egg_color == 'red':
        price_per_count = 13
    elif egg_color == 'green':
        price_per_count = 9
    else:
        price_per_count = 7

if egg_size == 'small':
    if egg_color == 'red':
        price_per_count = 9
    elif egg_color == 'green':
        price_per_count = 8
    else:
        price_per_count = 5

total_price = count * price_per_count
producion_cost = total_price * PRODUCTION_COST
final_price = total_price - producion_cost

print(f"{final_price:.2f} leva.")
