sum_prime = 0
sum_non_prime = 0
command = input()
while command != "stop":
    number = int(command)
    is_prime = True
    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    elif number == 0:
        command = input()
        continue

    for x in range(2, number):
        if number % x == 0:  # not prime
            is_prime = False
            break

    if is_prime:
        sum_prime += number
    else:
        sum_non_prime += number

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
