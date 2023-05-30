flour_price = float(input())
flour_qtity = float(input())
sugar_qtity = float(input())
eggs_cartons = int(input())
yeast_packets = int(input())

sugar_price = flour_price  - flour_price * 25 / 100
eggs_price = flour_price + flour_price * 10 / 100
yeast_price = sugar_price - sugar_price * 80 / 100


total_amount = flour_price * flour_qtity + sugar_qtity * sugar_price + eggs_cartons * eggs_price + yeast_packets * yeast_price

print(f"{total_amount:.2f}")