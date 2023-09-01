coins_of_1 = int(input())
coins_of_2 = int(input())
banknotes_of_5 = int(input())
value = int(input())

for coin_of_1 in range(coins_of_1 + 1):
    for coin_of_2 in range(coins_of_2 + 1):
        for banknote in range(banknotes_of_5 + 1):
            if coin_of_1 * 1 + coin_of_2 * 2 + banknote * 5 == value:
                print(f"{coin_of_1} * 1 lv. + {coin_of_2} * 2 lv. + {banknote} * 5 lv. = {value} lv.")
