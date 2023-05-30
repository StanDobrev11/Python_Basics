letter = ""

key_symbols_list = ["c", "n", "o"]
hidden_word = ""
is_finished = False
while not is_finished:
    letter = input()
    if letter == "End":
        is_finished = True
    elif ord(letter) in range(ord("A"), ord("Z") + 1) or ord(letter) in range(ord("a"), ord("z") + 1):
        if letter in key_symbols_list:
            key_symbols_list.remove(letter)
            if len(key_symbols_list) == 0:
                key_symbols_list = ["c", "n", "o"]
                print(hidden_word, end=" ")
                hidden_word = ""
        else:
            hidden_word += letter
