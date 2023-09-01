num_1_upper_limit = int(input())
num_2_upper_limit = int(input())
num_3_upper_limit = int(input())

pin_list = []

for a in range(1, num_1_upper_limit + 1):
    if a % 2 == 0:
        for b in range(1, num_2_upper_limit + 1):
            if b == 9:
                continue
            if b == 2:
                for c in range(1, num_3_upper_limit + 1):
                    if c % 2 == 0:
                        number = (str(a) + " " + str(b) + " " + str(c))
                        if number in pin_list:
                            continue
                        # print(number)
                        pin_list.append(number)

            for prime_check in range(2, b):
                if b % prime_check == 0:
                    break

                for c in range(1, num_3_upper_limit + 1):
                    if c % 2 == 0:
                        number = (str(a) + " " + str(b) + " " + str(c))
                        if number in pin_list:
                            continue
                        # print(number)
                        pin_list.append(number)

pin_list.sort()
for i in pin_list:
    print(i)
