# a се мени от 1 до 9
#  b се мени от 9 до а
#  c се мени от 0 до 9
#  d се мени от 9 до c
# Ако сумата (a + b + c + d) е равна на произведението (a * b * c * d) и едновременно с това n завършва на 5,
# трябва да се принтира числото abcd.
# Ако разделим произведението (a * b * c * d) на сумата (a + b + c + d) и получим 3 (целочислено), и
# едновременно с това n се дели на 3 без остатък, трябва да се принтира числото dcba.

n = int(input())

n_string = str(n)
is_found = False
for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(10):
            for d in range(9, c - 1, -1):
                if a + b + c + d == a * b * c * d and n_string[-1] == "5":
                    print(f"{a}{b}{c}{d}")
                    is_found = True
                    break
                elif a * b * c * d // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_found = True
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break
if not is_found:
    print("Nothing found")
