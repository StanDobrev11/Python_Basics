special_number = int(input())

for test_number in range(1111, 9999 + 1):
    test_number = str(test_number)
    if "0" in test_number:
        continue
    count = 0
    for symbol in test_number:
        if special_number % int(symbol) == 0:
            count += 1
            if count == 4:
                print(test_number, end=" ")
