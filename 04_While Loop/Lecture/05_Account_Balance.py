has_cash = True
account_amount = 0
while has_cash:
    cash = input()
    if cash == "NoMoreMoney":
        break

    cash = float(cash)
    if cash < 0:
        print("Invalid operation!")
        break
    else:
        account_amount += cash
        print(f"Increase: {cash :.2f}")

print(f"Total: {account_amount :.2f}")
