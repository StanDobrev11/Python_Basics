voucher_cost = int(input())

tickets_bought = 0
tickets_price = 0
item_price = 0
item_count = 0

voucher_left = voucher_cost
is_buying = True
while is_buying:
    purchase = input()
    if purchase == "End":
        break
    if len(purchase) > 8:
        tickets_price = ord(purchase[0]) + ord(purchase[1])
        if tickets_price > voucher_left:
            break
        else:
            tickets_bought += 1
            voucher_left -= tickets_price

    elif len(purchase) <= 8:
        item_price = ord(purchase[0])
        if item_price > voucher_left:
            break
        else:
            item_count += 1
            voucher_left -= item_price

print(f"{tickets_bought}")
print(f"{item_count}")

# both ASCII char commands
# print(chr(65))
# print(ord("A"))
