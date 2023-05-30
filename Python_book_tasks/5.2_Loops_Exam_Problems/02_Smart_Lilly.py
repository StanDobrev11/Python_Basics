current_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy = 0
lilly_money = 0
# FOR_BIRTHDAY = 10
for each_year in range(1, current_age + 1):
    if each_year % 2 == 1:
        toy += 1
    else:
        # lilly_money += FOR_BIRTHDAY - 1
        # FOR_BIRTHDAY += 10
        lilly_money += 10 * each_year / 2 - 1

toy_money = toy * toy_price
lilly_money += toy_money

# print(f"Yes! {(lilly_money - washing_machine_price):.2f}" if lilly_money >= washing_machine_price
#       else f"No! {(washing_machine_price - lilly_money):.2f}")
if lilly_money >= washing_machine_price:
    money_left = lilly_money - washing_machine_price
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = washing_machine_price - lilly_money
    print(f"No! {money_needed:.2f}")
