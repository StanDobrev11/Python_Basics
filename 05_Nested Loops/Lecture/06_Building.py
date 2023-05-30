decks = int(input())
rooms = int(input())
initial_decks = decks
# top deck
for room_num in range(rooms):
    print(f'L{decks}{room_num}', end=" ")
decks -= 1
print()
while decks > 0:
    for room_num in range(rooms):
        if decks % 2 == 0:
            print(f'O{decks}{room_num}', end=" ")
        else:
            print(f'A{decks}{room_num}', end=" ")
    print()
    decks -= 1
