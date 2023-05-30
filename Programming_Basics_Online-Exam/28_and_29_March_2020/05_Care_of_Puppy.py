food = int(input())
food = food * 1000

adopted = False
consumed = 0
while not adopted:
    per_day = input()
    if per_day == "Adopted":
        break
    consumed += int(per_day)


if food >= consumed:
    remaining_food = food - consumed
    print(f"Food is enough! Leftovers: {remaining_food} grams.")
else:
    required_food = consumed - food
    print(f"Food is not enough. You need {required_food} grams more.")
