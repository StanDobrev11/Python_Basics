change = float(input())
coins = 0
change = round(change * 100, 2)

# checking levs as coins
while change >= 200:
    change -= 200
    coins += 1
if change >= 100:
    change -= 100
    coins += 1

# checking pennies as coins
units = change % 10
change -= units
if units >= 5:
    units -= 5
    coins += 1
while units >= 2:
    units -= 2
    coins += 1
if units > 0:
    units -= 1
    coins += 1

# checking pennies * 10 as coins
tents = change / 10
if tents >= 5:
    tents -= 5
    coins += 1
while tents >= 2:
    tents -= 2
    coins += 1
if tents > 0:
    tents -= 1
    coins += 1

print(coins)
