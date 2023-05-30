player_name = input()

is_playing = True
SINGLE = 1
DOUBLE = 2
TRIPLE = 3
initial_score = 301
shots = 0
un_shots = 0
current_score = 0
while is_playing:
    field = input()
    if field == "Retire":
        print(f"{player_name} retired after {un_shots} unsuccessful shots.")
        break
    score = input()
    if score == "Retire":
        print(f"{player_name} retired after {un_shots} unsuccessful shots.")
        break
    else:
        score = int(score)


    if field == "Triple":
        score = score * TRIPLE
    if field == "Double":
        score = score * DOUBLE
    else:
        score = score

    current_score = current_score + score
    shots += 1
    if initial_score == current_score:
        print(f"{player_name} won the leg with {shots} shots.")
        is_playing = False
    if initial_score < current_score:
        un_shots += 1
        shots -= 1
        current_score = current_score - score