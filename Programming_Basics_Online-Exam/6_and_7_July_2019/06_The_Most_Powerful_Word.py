best_value = 0
best_word = ""

while True:
    word = input()
    if word == "End of words":
        break
    word_value = 0
    for i in word:
        word_value += ord(i)
    if word[0].lower() == "a" \
            or word[0].lower() == "e" \
            or word[0].lower() == "o" \
            or word[0].lower() == "i" \
            or word[0].lower() == "y" \
            or word[0].lower() == "u":
        word_value *= len(word)
    else:
        word_value /= len(word)

    if word_value > best_value:
        best_value = word_value
        best_word = word

print(f"The most powerful word is {best_word} - {int(best_value)}")
