favorite_book = input()
is_found = False
count = 0
while not is_found:
    book_name = input()
    count += 1
    if book_name == "No More Books":
        count -= 1
        print("The book you search is not here!\n"
              f"You checked {count} books.")
        break
    elif book_name == favorite_book:
        count -= 1
        print(f"You checked {count} books and found it.")
        break
