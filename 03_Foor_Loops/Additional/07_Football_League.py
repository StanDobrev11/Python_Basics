stadium_capacity = int(input())
fans = int(input())
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0
for _ in range(fans):
    location = input()
    if location == "A":
        sector_A += 1
    elif location == "B":
        sector_B += 1
    elif location == "V":
        sector_V += 1
    elif location == "G":
        sector_G += 1

print(f"{100 * sector_A / fans :.2f}%")
print(f"{100 * sector_B / fans :.2f}%")
print(f"{100 * sector_V / fans :.2f}%")
print(f"{100 * sector_G / fans :.2f}%")
print(f"{100 * fans / stadium_capacity :.2f}%")
