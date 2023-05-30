SMALL_SET = 2
LARGE_SET = 5

SMALL_WATERMELON = 56
SMALL_MANGO = 36.66
SMALL_PINEAPPLE = 42.10
SMALL_BERRY = 20

LARGE_WATERMELON = 28.70
LARGE_MANGO = 19.60
LARGE_PINEAPPLE = 24.80
LARGE_BERRY = 15.20

DISCOUNT_OVER_1000 = 0.5
DISCOUNT_OVER_400 = 0.15

fruit = input()
size_of_set = input()
how_many_sets = int(input())

total_price = 0
if fruit == "Mango":
    if size_of_set == "small":
        total_price = SMALL_SET * SMALL_MANGO * how_many_sets
    else:
        total_price = LARGE_SET * LARGE_MANGO * how_many_sets
elif fruit == "Watermelon":
    if size_of_set == "small":
        total_price = SMALL_SET * SMALL_WATERMELON * how_many_sets
    else:
        total_price = LARGE_SET * LARGE_WATERMELON * how_many_sets
elif fruit == "Pineapple":
    if size_of_set == "small":
        total_price = SMALL_SET * SMALL_PINEAPPLE * how_many_sets
    else:
        total_price = LARGE_SET * LARGE_PINEAPPLE * how_many_sets
elif fruit == "Raspberry":
    if size_of_set == "small":
        total_price = SMALL_SET * SMALL_BERRY * how_many_sets
    else:
        total_price = LARGE_SET * LARGE_BERRY * how_many_sets

if total_price > 1000:
    total_price = total_price * DISCOUNT_OVER_1000
elif total_price >= 400:
    total_price = total_price * (1 - DISCOUNT_OVER_400)

print(f"{total_price:.2f} lv.")
