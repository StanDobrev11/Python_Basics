from string import ascii_lowercase

n = int(input())
m = int(input())

for symbol_1 in range(1, n + 1):
    for symbol_2 in range(1, n + 1):
        for symbol_3 in range(m):
            symbol_3 = ascii_lowercase[symbol_3]
            for symbol_4 in range(m):
                symbol_4 = ascii_lowercase[symbol_4]
                for symbol_5 in range(1, n + 1):
                    if symbol_5 > symbol_2 and symbol_5 > symbol_1:
                        print(f"{symbol_1}{symbol_2}{symbol_3}{symbol_4}{symbol_5}", end=" ")
