age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys = 0
money_per_bday = 10
money_saved = 0
for year in range(1, age + 1):
    if year % 2 == 1:
        toys += 1
    else:
        money_saved += money_per_bday * year / 2
        money_saved -= 1

money_saved += toys * toy_price
if money_saved >= washing_machine_price:
    print(f"Yes! {money_saved - washing_machine_price :.2f}")
else:
    print(f"No! {abs(money_saved - washing_machine_price) :.2f}")
