BASKET = 1.5
WREATH = 3.8
BUNNY = 7
DISCOUNT = 20 / 100

customer = int(input())
ttl_count = 0
ttl_price = 0
for each in range(customer):
    basket = 0
    wreath = 0
    bunny = 0
    finished = False
    while not finished:
        purchase = input().lower()
        if purchase == 'basket':
            basket += 1
        if purchase == 'wreath':
            wreath += 1
        if purchase == 'chocolate bunny':
            bunny += 1
        if purchase == 'finish':
            price_per_customer = basket * BASKET + wreath * WREATH + bunny * BUNNY
            count_of_purchase = basket + wreath + bunny
            if count_of_purchase % 2 == 0:
                price_per_customer = price_per_customer - price_per_customer * DISCOUNT
                print(f"You purchased {count_of_purchase} items for {price_per_customer:.2f} leva.")
            ttl_price = ttl_price + price_per_customer
            finished = True

average_price = ttl_price / customer
print(f"Average bill per client is: {average_price:.2f} leva.")  
