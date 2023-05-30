import datetime as dt
from time import process_time

initial_year = int(input())
end_year = int(input())
seek_weight = int(input())

# start = time.time()
if end_year == initial_year:  # converting end year in format yyyy-mm-dd
    end_year = dt.date(end_year + 1, 1, 1)
else:
    end_year = dt.date(end_year, 12, 31)

initial_year = dt.date(initial_year, 1, 1)  # converting initial year in format yyyy-mm-dd

time_diff = end_year - initial_year
time_change = dt.timedelta(1)  # adjusting day change by adding one (1) day

is_valid = False  # checking if valid year according to given weight is found
for day in range(time_diff.days + 1):  # checking for each day if the date is valid
    initial_date = (initial_year + dt.timedelta(day)).strftime("%d-%m-%Y")  # converting date to dd-mm-yyyy format
    date = str(initial_date)
    date = date.replace("-", "")
    year_weight = 0
    for x in range(len(date)):  # multiplication of each item by each item
        for y in range(x + 1, len(date)):
            year_weight += int(date[x]) * int(date[y])
    if year_weight == seek_weight:
        print(initial_date)
        is_valid = True

if not is_valid:
    print("No")

# end = time.time()
# print(end - start)
# print(time.time_ns())
# print(process_time())
