GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

DISCOUNT_PER_GASOLINE = 0.18
DISCOUNT_PER_DIESEL = 0.12
DISCOUNT_PER_GAS = 0.08

DISCOUNT_IF_MORE_THAN_20LTRS = 0.08  # PERCENT OF FINAL COST
DISCOUNT_IF_MORE_THAN_25LTRS = 0.10  # PERCENT OF FINAL COST

type_of_fuel = input()
fuel_quantity = float(input())
discount_card = input()

cost = 0
if type_of_fuel == "Gasoline":
    cost = fuel_quantity * GASOLINE_PRICE
    if discount_card == "Yes":
        cost = fuel_quantity * (GASOLINE_PRICE - DISCOUNT_PER_GASOLINE)
elif type_of_fuel == "Diesel":
    cost = fuel_quantity * DIESEL_PRICE
    if discount_card == "Yes":
        cost = fuel_quantity * (DIESEL_PRICE - DISCOUNT_PER_DIESEL)
elif type_of_fuel == "Gas":
    cost = fuel_quantity * GAS_PRICE
    if discount_card == "Yes":
        cost = fuel_quantity * (GAS_PRICE - DISCOUNT_PER_GAS)

if fuel_quantity >= 25:
    cost = cost - cost * DISCOUNT_IF_MORE_THAN_25LTRS
elif fuel_quantity >= 20:
    cost = cost - cost * DISCOUNT_IF_MORE_THAN_20LTRS

print(f"{cost:.2f} lv.")
