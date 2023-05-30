JIGSAW = 2.60
TALKING_DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

trip_price = float(input())
jigsaw_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_cash = jigsaw_count * JIGSAW + \
             dolls_count * TALKING_DOLL + \
             bears_count * TEDDY_BEAR + \
             minion_count * MINION + \
             truck_count * TRUCK

total_count = jigsaw_count + dolls_count + bears_count + minion_count + truck_count

if total_count >= 50:
    total_cash = total_cash - total_cash / 4

rent = total_cash * 0.1
cash_rob = total_cash - rent - trip_price


if cash_rob >= 0:
    print(f"Yes! {cash_rob:.2f} lv left.")
else:
    print(f"Not enough money! {abs(cash_rob):.2f} lv needed.")
