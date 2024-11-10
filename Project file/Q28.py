import calendar

def is_leap_year(year):
    return calendar.isleap(year)

def count_leap_days(start_year, end_year):
    leap_days = sum(1 for year in range(start_year, end_year + 1) if is_leap_year(year))
    return leap_days

year = int(input("Enter a year to check if it's a leap year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

leap_days_1950_2000 = count_leap_days(1950, 2000)
print("Number of leap days between 1950 and 2000:", leap_days_1950_2000)
