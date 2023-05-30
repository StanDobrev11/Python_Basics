product_type = input()

fruit_list = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegies_list = ["tomato", "cucumber", "pepper", "carrot"]

if product_type in fruit_list:
    print("fruit")
elif product_type in vegies_list:
    print("vegetable")
else:
    print("unknown")
