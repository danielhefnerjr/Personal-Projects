month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 1 # start on Monday January 1 1900 -- Sunday will be 0 mod 7

sundays = 0
for year in range(1900,2001):
    for month in range(0,12):
        if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day += 29
        else:
            day += month_days[month]

        if year >= 1901 and day % 7 == 0: # start counting at 1901
            sundays += 1

print(sundays)
