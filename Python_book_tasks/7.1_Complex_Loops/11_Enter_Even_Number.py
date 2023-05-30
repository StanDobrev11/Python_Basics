while True:
    n = int(input("Enter even number: "))
    if n % 2 != 0:
        print("The number is not even")
    else:
        print(f"Even number entered: {n}")
        break
