animal = input()

reptile_list = ["crocodile", "tortoise", "snake"]

if animal == "dog":
    print("mammal")
elif animal in reptile_list:
    print("reptile")
else:
    print("unknown")
