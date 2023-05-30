expression = input()
#expression = "4 + 6 / 5 + 4 * 9 - 8 / 7 * 2 ="
# expression = "(4 + 6 / 5 + 4 * 9 - 8 / 7 * 2) ="

expression = list(expression)
# expression.pop()
for symbol in expression:
    if symbol == " ":
        expression.remove(symbol)

current_result = 0
operator = "+"
symbol = ""
while symbol != "=":
    symbol = expression[0]
    if symbol == "(":
        expression.pop(0)
        inner_result = 0
        inner_operator = "+"
        for next_symbol in expression:
            while next_symbol != ")":
                expression.pop(0)
                if ord(next_symbol) in range(48, 58):
                    if inner_operator == "+":
                        inner_result += int(next_symbol)
                    elif inner_operator == "-":
                        inner_result -= int(next_symbol)
                    elif inner_operator == "*":
                        inner_result *= int(next_symbol)
                    elif inner_operator == "/":
                        inner_result /= int(next_symbol)
                elif (next_symbol == "+") or (next_symbol == "-") or (next_symbol == "*") or (next_symbol == "/"):
                    if next_symbol == "+":
                        inner_operator = "+"
                    elif next_symbol == "-":
                        inner_operator = "-"
                    elif next_symbol == "*":
                        inner_operator = "*"
                    elif next_symbol == "/":
                        inner_operator = "/"
                next_symbol = expression[0]

            if operator == "+":
                current_result += inner_result
            elif operator == "-":
                current_result -= inner_result
            elif operator == "*":
                current_result *= inner_result
            elif operator == "/":
                current_result /= inner_result
            break

    elif ord(symbol) in range(48, 58):  # 48 - 58
        if operator == "+":
            current_result += int(symbol)
        elif operator == "-":
            current_result -= int(symbol)
        elif operator == "*":
            current_result *= int(symbol)
        elif operator == "/":
            current_result /= int(symbol)
    elif (symbol == "+") or (symbol == "-") or (symbol == "*") or (symbol == "/"):
        if symbol == "+":
            operator = "+"
        elif symbol == "-":
            operator = "-"
        elif symbol == "*":
            operator = "*"
        elif symbol == "/":
            operator = "/"
    expression.pop(0)
# print(brackets)
# print(expression)
# print(inner_result)
print(f"{current_result:.2f}")
