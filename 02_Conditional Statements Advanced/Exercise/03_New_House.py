flower_prices = {"Roses": 5, "Dahlias": 3.8, "Tulips": 2.8, "Narcissus": 3, "Gladiolus": 2.5}
discount_range = {"Roses": 10, "Dahlias": 15, "Tulips": 15, "Narcissus": 15, "Gladiolus": 20}
discount_qtity = {"Roses": 80, "Dahlias": 90, "Tulips": 80}
more_expensive = {"Narcissus": 120, "Gladiolus": 80}

flower_type = input()
flower_count = int(input())
budget = int(input())

amount_required = 0
if flower_type in discount_qtity:
    if flower_count > discount_qtity[flower_type]:
        amount_required = flower_prices[flower_type] * flower_count * (100 - discount_range[flower_type]) / 100
    else:
        amount_required = flower_prices[flower_type] * flower_count
elif flower_type in more_expensive:
    if flower_count < more_expensive[flower_type]:
        amount_required = flower_prices[flower_type] * flower_count * (100 + discount_range[flower_type]) / 100
    else:
        amount_required = flower_prices[flower_type] * flower_count

if budget >= amount_required:
    remaining_cash = budget - amount_required
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {remaining_cash:.2f} leva left.")
else:
    cash_needed = amount_required - budget
    print(f"Not enough money, you need {cash_needed:.2f} leva more.")
