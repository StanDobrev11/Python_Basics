# ABxyBA |

x_upper_range = int(input())
y_upper_range = int(input())
max_passwords_to_be_generated = int(input())

symbol_A = 35
symbol_B = 64
count = 0
for x in range(1, x_upper_range + 1):
    for y in range(1, y_upper_range + 1):
        if count >= max_passwords_to_be_generated:
            break
        print(f"{chr(symbol_A)}{chr(symbol_B)}{x}{y}{chr(symbol_B)}{chr(symbol_A)}", end="|")
        count += 1
        symbol_A += 1
        symbol_B += 1
        if symbol_A > 55:
            symbol_A = 35
        if symbol_B > 96:
            symbol_B = 64

