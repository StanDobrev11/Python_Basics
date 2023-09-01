control_value = int(input())

count = 0
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and c > d) and a * b + c * d == control_value:
                    number_checked = f"{a}{b}{c}{d}"
                    print(number_checked, end=" ")
                    count += 1
                    if count == 4:
                        password = number_checked

if count >= 4:
    print()
    print(f"Password: {password}")
elif count > 0:
    print()
    print("No!")
else:
    print("No!")
