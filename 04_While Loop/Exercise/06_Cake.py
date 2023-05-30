width = int(input())
length = int(input())

ttl_pieces = width * length
is_finished = False

while not is_finished:
    command = input()
    if command == "STOP":
        break
    else:
        pieces = int(command)
        ttl_pieces -= pieces
        if ttl_pieces <= 0:
            is_finished = True

if is_finished:
    print(f"No more cake left! You need {abs(ttl_pieces)} pieces more.")
else:
    print(f"{ttl_pieces} pieces are left.")
