annual_fee = int(input())

sneackers_price = annual_fee - annual_fee * 0.4
equipment = sneackers_price - sneackers_price * 0.20
ball = equipment * 0.25
accessoaries = ball * 0.20

total_cost = annual_fee + sneackers_price + equipment + ball + accessoaries

print(f"{total_cost:.2f}")