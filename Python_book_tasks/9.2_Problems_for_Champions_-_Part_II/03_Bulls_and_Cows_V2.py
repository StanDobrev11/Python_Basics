from random import choice

secret_number = "3574"
secret_number = tuple(secret_number)

numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
available_numbers = list(numbers)

guessed_numbers = []
for index in range(4):
    number = choice(available_numbers)
    available_numbers.remove(number)
    guessed_numbers.append(number)

# print(*guessed_numbers, sep="")

cow = 2
bull = 0
# number = input()
# number = list(number)
for index, symbol in enumerate(guessed_numbers):
    if symbol in secret_number:
        cow += 1
        if guessed_numbers[index] == secret_number[index]:
            cow -= 1
            bull += 1
print(*secret_number, sep="")
print(f"Cows: {cow}, Bulls: {bull}")
print("".join(guessed_numbers))
# def computer_random_number(attempt):
#     guessed_number = ""
#
#     if attempt > 1:
#         is_valid = False
#         while not is_valid:
#             guessed_number = random.randint(1234, 9876)
#             guessed_number = str(guessed_number)
#             if guessed_number[0] != guessed_number[1] and \
#                     guessed_number[0] != guessed_number[2] and \
#                     guessed_number[0] != guessed_number[3] and \
#                     guessed_number[1] != guessed_number[2] and \
#                     guessed_number[1] != guessed_number[3] and \
#                     guessed_number[2] != guessed_number[3] and \
#                     guessed_number[0] != "0" and \
#                     guessed_number[1] != "0" and \
#                     guessed_number[2] != "0" and \
#                     guessed_number[3] != "0":
#                 is_valid = True
#
#     elif attempt > 0:
#         guessed_number = "5678"
#     elif attempt == 0:
#         guessed_number = "1234"
#
#     print(guessed_number)


