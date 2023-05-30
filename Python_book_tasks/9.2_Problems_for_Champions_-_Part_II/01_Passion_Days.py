from decimal import Decimal

initial_amount = Decimal(input())
cash_left = initial_amount
command = input()  # "mall.Enter" & "mall.Exit"
purchase_count = 0
while command != "mall.Enter":
    command = input()

command = input()
while command != "mall.Exit":
    string = command
    for symbol in string:
        if symbol == "%":
            cost = Decimal(cash_left / 2)
        elif symbol == "*":
            cost = -10
        elif symbol.isupper():
            cost = Decimal(ord(symbol) * 0.5)
        elif symbol.islower():
            cost = Decimal(ord(symbol) * 0.3)
        else:
            cost = Decimal(ord(symbol))
        if Decimal(cash_left) < Decimal(cost):
            continue
        cash_left -= Decimal(cost)
        if symbol != "*":
            purchase_count += 1
    command = input()

if command == "mall.Exit":
    if purchase_count > 0:
        print(f"{purchase_count} purchases. Money left: {cash_left:.2f} lv.")
    else:
        print(f"No purchases. Money left: {cash_left:.2f} lv.")
