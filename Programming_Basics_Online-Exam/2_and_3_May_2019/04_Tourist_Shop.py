budget = float(input())

is_stop = False
is_expensive = False
product_count = 0
total_cost = 0
current_budget = 0
while not is_stop and not is_expensive:
    product = input()
    if product == "Stop":
        print(f"You bought {product_count} products for {total_cost:.2f} leva.")
        break
        # is_stop = True
    else:
        product_price = float(input())
        product_count += 1
        if product_count % 3 == 0:
            product_price = product_price / 2
        total_cost += product_price
        current_budget = budget - total_cost
        if current_budget < 0:
            total_cost -= product_price
            product_count -= 1
            print(f"You don't have enough money!\n"
                  f"You need {abs(current_budget):.2f} leva!")
            break
            # is_expensive = True

# if is_stop:
#     print(f"You bought {product_count} products for {total_cost:.2f} leva.")
# elif is_expensive:
#     print(f"You don't have enough money!\n"
#           f"You need {abs(current_budget):.2f} leva!")
