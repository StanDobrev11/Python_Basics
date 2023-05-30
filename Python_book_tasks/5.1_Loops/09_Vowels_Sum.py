A = 1
E = 2
I = 3
O = 4
U = 5

word = input()

sum_vowels = 0
for letter in word:
    if letter == "a":
        sum_vowels += A
    if letter == "e":
        sum_vowels += E
    if letter == "i":
        sum_vowels += I
    if letter == "o":
        sum_vowels += O
    if letter == "u":
        sum_vowels += U

print(sum_vowels)

