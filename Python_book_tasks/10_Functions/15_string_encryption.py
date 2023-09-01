def encrypt(symbol):
    letter_ord = ord(symbol)
    symbol_2 = str(ord(symbol))
    symbol_2 = symbol_2[0] + symbol_2[-1]
    symbol_1 = letter_ord + int(symbol_2[-1])
    symbol_3 = int(ord(symbol))
    symbol_3 = letter_ord - int(symbol_2[0])
    code = f"{chr(symbol_1)}{symbol_2}{chr(symbol_3)}"

    return code


result = ""
entries = int(input())
for _ in range(entries):
    letter = input()
    result += encrypt(letter)

print(result)
