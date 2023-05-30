month = input()
days_stay = int(input())

studio_monthly_price = {"may_october": 50, "june_september": 75.2, "july_august": 76}
apartment_monthly_price = {"may_october": 65, "june_september": 68.7, "july_august": 77}

months = ""
if month == "May" or month == "October":
    months = "may_october"
elif month == "June" or month == "September":
    months = "june_september"
elif month == "July" or month == "August":
    months = "july_august"

studio_cost = studio_monthly_price[months] * days_stay
apartment_cost = apartment_monthly_price[months] * days_stay

if days_stay > 14:
    apartment_cost *= (1 - 0.1)
    if months == "may_october":
        studio_cost *= (1 - 0.3)
    elif months == "june_september":
        studio_cost *= (1 - 0.2)
elif days_stay > 7 and months == "may_october":
    studio_cost *= (1 - 0.05)

print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
