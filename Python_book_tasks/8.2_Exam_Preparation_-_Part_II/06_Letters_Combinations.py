initial_letter = input()
last_letter = input()
letter_to_skip = input()

count = 0
for first_symbol in range(ord(initial_letter), ord(last_letter) + 1):
    for second_symbol in range(ord(initial_letter), ord(last_letter) + 1):
        for third_symbol in range(ord(initial_letter), ord(last_letter) + 1):
            if chr(first_symbol) != letter_to_skip and \
                    chr(second_symbol) != letter_to_skip and \
                    chr(third_symbol) != letter_to_skip:
                print(f"{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}", end=" ")
                count += 1
print(count)
