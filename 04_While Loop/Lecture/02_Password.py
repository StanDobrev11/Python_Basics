user = input()
set_password = input()

is_false = True
while is_false:
    password = input()
    if password == set_password:
        print(f"Welcome {user}!")
        is_false = False
  