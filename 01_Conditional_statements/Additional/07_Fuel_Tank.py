type_of_fuel = input()
fuel_quantity = float(input())

if type_of_fuel != "Diesel" and type_of_fuel != "Gas" and type_of_fuel != "Gasoline":
    print("Invalid fuel!")
elif fuel_quantity >= 25:
    print(f"You have enough {type_of_fuel.lower()}.")
else:
    print(f"Fill your tank with {type_of_fuel.lower()}!")
