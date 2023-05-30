a1 = int(input())
a2 = int(input())
n = int(input())

for a in range(a1, a2):
    symbol_1 = chr(a)
    for b in range(1, n):
        symbol_2 = b
        for c in range(1, int(n / 2)):
            symbol_3 = c
            symbol_4 = a
            if a % 2 == 1 and (a + b + c) % 2 == 1:
                print(f"{str(symbol_1)}-{str(symbol_2)}{str(symbol_3)}{str(symbol_4)}")
