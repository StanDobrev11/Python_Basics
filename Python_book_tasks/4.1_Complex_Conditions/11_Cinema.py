PREMIERE = 12
NORMAL = 7.5
DISCOUNT = 5  # прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

type_of_movie = input()
rows = int(input())
columns = int(input())

seats = rows * columns

profit = 0
if type_of_movie == "Premiere":
    profit = seats * PREMIERE
elif type_of_movie == "Normal":
    profit = seats * NORMAL
else:
    profit = seats * DISCOUNT

print(f"{profit:.2f}")
