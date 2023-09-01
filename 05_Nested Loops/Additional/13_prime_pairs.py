def prime_check(number):
    is_prime = True
    if number <= 0:
        return False
    elif number == 1:
        return True
    else:
        for x in range(2, number):
            if number % x == 0:  # not prime
                is_prime = False
        if is_prime:
            return True
        else:
            return False


first_pair_start_range = int(input())
second_pair_start_range = int(input())
first_pair_range = int(input())
second_pair_range = int(input())

first_pair_end_range = first_pair_start_range + first_pair_range
second_pair_end_range = second_pair_start_range + second_pair_range

for pair_1 in range(first_pair_start_range, first_pair_end_range + 1):
    for pair_2 in range(second_pair_start_range, second_pair_end_range + 1):
        if prime_check(pair_1) and prime_check(pair_2):
            print(f"{pair_1}{pair_2}")
