screening_type = input()
rows = int(input())
col = int(input())

PREMIERE_PRICE = 12
NORMAL_PRICE = 7.5
DISCOUNT = 5

profit = 0
if screening_type == "Premiere":
    profit = rows * col * PREMIERE_PRICE
elif screening_type == "Normal":
    profit = rows * col * NORMAL_PRICE
elif screening_type == "Discount":
    profit = rows * col * DISCOUNT

print(f"{profit:.2f}")
