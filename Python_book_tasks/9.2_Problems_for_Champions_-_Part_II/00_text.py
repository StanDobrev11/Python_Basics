from random import choice


def random_number():
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    available_numbers = list(numbers)

    guessed_numbers = []
    for index in range(4):
        number = choice(available_numbers)
        available_numbers.remove(number)
        guessed_numbers.append(number)

    return "".join(guessed_numbers)


def computer_guess(bulls, cows, comp_number):
    count = 0
    # if count == 0:
    # is_solution_found = False

    # else:
    #     comp_number = choice(number_out_of_list)
    number_generated_list = []
    for num_1 in range(1, 10):
        for num_2 in range(1, 10):
            for num_3 in range(1, 10):
                for num_4 in range(1, 10):
                    if num_1 != 0 and num_2 != 0 and num_3 != 0 and num_4 != 0 and num_1 != num_2 and num_1 != num_3 and num_1 != num_4 and num_2 != num_3 and num_2 != num_4 and num_3 != num_4:
                        bulls_found = 0
                        cows_found = 0
                        number_generated = (num_1, num_2, num_3, num_4)
                        number_to_check = list(number_generated)
                        guessed_number = list(comp_number)

                        for index in range(4):  # checking bulls
                            if number_to_check[index] == int(guessed_number[index]):
                                bulls_found += 1
                                number_to_check[index] = index - 10
                                guessed_number[index] = index - 100

                        for i in range(4):  # checking cows
                            if int(guessed_number[i]) in number_to_check:
                                cows_found += 1
                                index = number_to_check.index(int(guessed_number[i]))
                                number_to_check[index] = index - 50

                        if bulls_found == int(bulls) and cows_found == int(cows):
                            output_number = [str(i) for i in number_generated]
                            number_generated_list.append("".join(output_number))
                            # print(*number_generated, sep="", end=" ")
                            # is_solution_found = True

    return number_generated_list


comp_number = random_number()
print(comp_number)
result = computer_guess(input("Bulls: "), input("Cows: "), comp_number)
comp_number = choice(result)
print(comp_number)
print(len(result))
result = computer_guess(input("Bulls: "), input("Cows: "), comp_number)
comp_number = choice(result)
print(comp_number)
print(len(result))
result = computer_guess(input("Bulls: "), input("Cows: "), comp_number)
comp_number = choice(result)
print(comp_number)
print(len(result))
result = computer_guess(input("Bulls: "), input("Cows: "), comp_number)
comp_number = choice(result)
print(comp_number)
print(len(result))
result = computer_guess(input("Bulls: "), input("Cows: "), comp_number)
comp_number = choice(result)
print(comp_number)
print(len(result))
# if not is_solution_found:
#     print("No")
