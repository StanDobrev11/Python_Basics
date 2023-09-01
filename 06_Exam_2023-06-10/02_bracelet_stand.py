pocket_money_per_day = float(input())
profit_per_day = float(input())
expenses_per_5_days = float(input())
present_price = float(input())

saved_fm_pocket_money = 5 * pocket_money_per_day
saved_fm_sales = 5 * profit_per_day

money_saved = saved_fm_pocket_money + saved_fm_sales - expenses_per_5_days

if money_saved >= present_price:
    print(f"Profit: {money_saved :.2f} BGN, the gift has been purchased.")
else:
    money_needed = present_price - money_saved
    print(f"Insufficient money: {money_needed :.2f} BGN.")
