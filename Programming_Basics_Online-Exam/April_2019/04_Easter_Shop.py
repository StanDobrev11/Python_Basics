eggs_count = int(input())

is_opened = True
eggs_sold = 0

while is_opened:

    buy_or_refill = input().lower()
    if buy_or_refill == 'close':
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    qtity = input()
    if qtity == 'close':
        is_opened = False
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
    else:
        qtity = int(qtity)

    if buy_or_refill == 'buy':
        eggs_count = eggs_count - qtity
        if eggs_count < 0:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_count + qtity}.")
            break
        eggs_sold = eggs_sold + qtity

    elif buy_or_refill == 'fill':
        eggs_count = eggs_count + qtity