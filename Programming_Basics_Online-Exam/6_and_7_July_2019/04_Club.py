target_profit = float(input())

is_party = False
is_enough = False
cash_made = 0
while not is_enough and not is_party:
    cocktail_name = input()
    if cocktail_name == "Party!":
        is_party = True
    else:
        how_many_cocktails = int(input())
        cocktail_price = len(cocktail_name)
        cash_for_order = cocktail_price * how_many_cocktails
        if cash_for_order % 2 == 1:
            cash_for_order -= 0.25 * cash_for_order
        cash_made += cash_for_order
        if cash_made >= target_profit:
            is_enough = True

if is_party:
    cash_needed = target_profit - cash_made
    print(f"We need {cash_needed:.2f} leva more.\n"
          f"Club income - {cash_made:.2f} leva.")
elif is_enough:
    print(f"Target acquired.\n"
          f"Club income - {cash_made:.2f} leva.")
