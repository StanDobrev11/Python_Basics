days = int(input())
total_food = float(input())

cookies = 0
dog_eats = 0
cat_eats = 0
for each_day in range(1, days + 1):
    dog = int(input())
    cat = int(input())
    per_day = dog + cat
    dog_eats += dog
    cat_eats += cat
    if each_day % 3 == 0:
        cookies += 0.1 * per_day

food_left = total_food - (dog_eats + cat_eats)
food_eaten = dog_eats + cat_eats
percent_food_eaten = 100 * (total_food - food_left) / total_food
percent_food_eaten_by_dog = 100 * (dog_eats / food_eaten)
percent_food_eaten_by_cat = 100 * (cat_eats / food_eaten)

print(f"Total eaten biscuits: {cookies:.0f}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_food_eaten_by_dog:.2f}% eaten from the dog.")
print(f"{percent_food_eaten_by_cat:.2f}% eaten from the cat.")
