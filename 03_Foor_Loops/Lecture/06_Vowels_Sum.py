vowels_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

string = input()

total_sum = 0
for letter in string:
    if letter in vowels_dict:
        total_sum += vowels_dict[letter]

print(total_sum)
