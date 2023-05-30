MAY_OCTOBER_STUDIO = 50
JUNE_SEPTEMBER_STUDIO = 75.2
JULY_AUGUST_STUDIO = 76
MAY_OCTOBER_APARTMENT = 65
JUNE_SEPTEMBER_APARTMENT = 68.7
JULY_AUGUST_APARTMENT = 77

DISCOUNT_STUDIO_7_OR_MORE_MAY_OCTOBER = 0.05
DISCOUNT_STUDIO_14_OR_MORE_MAY_OCTOBER = 0.3
DISCOUNT_STUDIO_14_OR_MORE_JUNE_SEPTEMBER = 0.2
DISCOUNT_APARTMENT_14_OR_MORE = 0.1

month_of_stay = input()
nights_stay = int(input())

studio_costs = 0
apartment_costs = 0
if month_of_stay == "May" or month_of_stay == "October":
    if nights_stay > 14:
        studio_costs = nights_stay * MAY_OCTOBER_STUDIO * (1 - DISCOUNT_STUDIO_14_OR_MORE_MAY_OCTOBER)
        apartment_costs = nights_stay * MAY_OCTOBER_APARTMENT * (1 - DISCOUNT_APARTMENT_14_OR_MORE)
    elif nights_stay > 7:
        studio_costs = nights_stay * MAY_OCTOBER_STUDIO * (1 - DISCOUNT_STUDIO_7_OR_MORE_MAY_OCTOBER)
        apartment_costs = nights_stay * MAY_OCTOBER_APARTMENT
    else:
        studio_costs = nights_stay * MAY_OCTOBER_STUDIO
        apartment_costs = nights_stay * MAY_OCTOBER_APARTMENT
elif month_of_stay == "June" or month_of_stay == "September":
    if nights_stay > 14:
        studio_costs = nights_stay * JUNE_SEPTEMBER_STUDIO * (1 - DISCOUNT_STUDIO_14_OR_MORE_JUNE_SEPTEMBER)
        apartment_costs = nights_stay * JUNE_SEPTEMBER_APARTMENT * (1 - DISCOUNT_APARTMENT_14_OR_MORE)
    else:
        studio_costs = nights_stay * JUNE_SEPTEMBER_STUDIO
        apartment_costs = nights_stay * JUNE_SEPTEMBER_APARTMENT
elif month_of_stay == "July" or month_of_stay == "August":
    if nights_stay > 14:
        studio_costs = nights_stay * JULY_AUGUST_STUDIO
        apartment_costs = nights_stay * JULY_AUGUST_APARTMENT * (1 - DISCOUNT_APARTMENT_14_OR_MORE)
    else:
        studio_costs = nights_stay * JULY_AUGUST_STUDIO
        apartment_costs = nights_stay * JULY_AUGUST_APARTMENT

print(f"Apartment: {apartment_costs:.2f} lv.")
print(f"Studio: {studio_costs:.2f} lv.")
