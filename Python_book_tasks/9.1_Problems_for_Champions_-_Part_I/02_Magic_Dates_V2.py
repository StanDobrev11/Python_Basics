import datetime as dt
from time import process_time

initial_year = int(input())
end_year = int(input())
seek_weight = int(input())

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
    d0 = int(date[0])
    d1 = int(date[1])
    d2 = int(date[2])
    d3 = int(date[3])
    d4 = int(date[4])
    d5 = int(date[5])
    d6 = int(date[6])
    d7 = int(date[7])
    year_weight = d0 * (d1 + d2 + d3 + d4 + d5 + d6 + d7) + \
                  d1 * (d2 + d3 + d4 + d5 + d6 + d7) + \
                  d2 * (d3 + d4 + d5 + d6 + d7) + \
                  d3 * (d4 + d5 + d6 + d7) + \
                  d4 * (d5 + d6 + d7) + \
                  d5 * (d6 + d7) + \
                  d6 * d7

    if year_weight == seek_weight:
        print(initial_date)
        is_valid = True

if not is_valid:
    print("No")
print(process_time())