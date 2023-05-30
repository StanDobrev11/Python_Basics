from random import randint


# def comp_random_number():
#     random_number_guess = ""
#     is_valid = False
#     while not is_valid:
#         random_number_guess = randint(1234, 9876)
#         random_number_guess = str(random_number_guess)
#         if random_number_guess[0] != random_number_guess[1] and \
#                 random_number_guess[0] != random_number_guess[2] and \
#                 random_number_guess[0] != random_number_guess[3] and \
#                 random_number_guess[1] != random_number_guess[2] and \
#                 random_number_guess[1] != random_number_guess[3] and \
#                 random_number_guess[2] != random_number_guess[3] and \
#                 random_number_guess[0] != "0" and \
#                 random_number_guess[1] != "0" and \
#                 random_number_guess[2] != "0" and \
#                 random_number_guess[3] != "0":
#             is_valid = True
#     return random_number_guess


# def computer_guess(bulls, cows):
count = 0
is_solution_found = False
# comp_random_number()
for num_1 in range(1, 10):
    for num_2 in range(1, 10):
        for num_3 in range(1, 10):
            for num_4 in range(1, 10):
                if num_1 != 0 and num_2 != 0 and num_3 != 0 and num_4 != 0 and num_1 != num_2 and num_1 != num_3 and num_1 != num_4 and num_2 != num_3 and num_2 != num_4 and num_3 != num_4:
                    bulls_found = 0
                    cows_found = 0
                    number_generated = (num_1, num_2, num_3, num_4)
                    number_to_check = list(number_generated)
                    guessed_number = list(comp_random_number())
                    # checking bulls
                    for index in range(4):
                        if number_to_check[index] == int(guessed_number[index]):
                            bulls_found += 1
                            number_to_check[index] = index - 10
                            guessed_number[index] = index - 100
                    # checking cows
                    for i in range(4):
                        if int(guessed_number[i]) in number_to_check:
                            cows_found += 1
                            index = number_to_check.index(int(guessed_number[i]))
                            number_to_check[i] = i - 10

computer_guess()
# print()
# print(count)
# if not is_solution_found:
#     print("No")
