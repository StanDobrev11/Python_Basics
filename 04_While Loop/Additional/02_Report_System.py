goal_profit = int(input())

is_profit_reached = False
payment_count = 0
total_profit = 0
count_in_cash = 0
count_by_card = 0
total_in_cash = 0
total_by_card = 0
while not is_profit_reached:
    command = input()
    if command == "End":
        break
    else:
        payment_count += 1
        item_price = int(command)
        if payment_count % 2 == 1:
            if item_price > 100:
                print("Error in transaction!")
            else:
                print("Product sold!")
                total_in_cash += item_price
                total_profit += item_price
                count_in_cash += 1
        elif payment_count % 2 == 0:
            if item_price < 10:
                print("Error in transaction!")
            else:
                print("Product sold!")
                total_by_card += item_price
                total_profit += item_price
                count_by_card += 1
    if total_profit >= goal_profit:
        is_profit_reached = True


if is_profit_reached:
    print(f"Average CS: {total_in_cash / count_in_cash :.2f}")
    print(f"Average CC: {total_by_card / count_by_card :.2f}")

else:
    print("Failed to collect required money for charity.")
