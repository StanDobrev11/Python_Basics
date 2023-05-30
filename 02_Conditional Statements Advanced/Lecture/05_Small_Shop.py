product = input()
city = input()
qtity = float(input())

products = {"coffee": 0, "water": 1, "beer": 2, "sweets": 3, "peanuts": 4}

sofia_product_price = [0.50, 0.80, 1.20, 1.45, 1.60]
plovdiv_product_price = [0.40, 0.70, 1.15, 1.30, 1.50]
varna_product_price = [0.45, 0.70, 1.10, 1.35, 1.55]

total_price = 0
if city == "Sofia":
    total_price = qtity * sofia_product_price[products[product]]
elif city == "Varna":
    total_price = qtity * varna_product_price[products[product]]
elif city == "Plovdiv":
    total_price = qtity * plovdiv_product_price[products[product]]
else:
    print("Error")

print(total_price)
