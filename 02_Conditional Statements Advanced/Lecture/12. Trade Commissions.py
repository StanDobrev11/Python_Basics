sales_range = {"to_500": 0,
               "to_1000": 1,
               "to_10000": 2,
               "more_than_10000": 3}
sofia_com = [5, 7, 8, 12]
varna_com = [4.5, 7.5, 10, 13]
plovdiv_com = [5.5, 8, 12, 14.5]

city = input()
sales = float(input())

is_error = False
sales_percent = 0
if sales > 10000:
    sales_percent = "more_than_10000"
elif sales > 1000:
    sales_percent = "to_10000"
elif sales > 500:
    sales_percent = "to_1000"
elif sales > 0:
    sales_percent = "to_500"
else:
    is_error = True

commission = 0
if city == "Sofia" and not is_error:
    commission = sales * sofia_com[sales_range[sales_percent]] / 100
elif city == "Varna" and not is_error:
    commission = sales * varna_com[sales_range[sales_percent]] / 100
elif city == "Plovdiv" and not is_error:
    commission = sales * plovdiv_com[sales_range[sales_percent]] / 100
else:
    is_error = True

if is_error:
    print("error")
else:
    print(f"{commission:.2f}")
