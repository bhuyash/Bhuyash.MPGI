import calendar

def display_month_calendar(year, month):
    print("Calendar for", calendar.month_name[month], year)
    print(calendar.month(year, month))

def display_year_calendar(year):
    print("Calendar for the year", year)
    print(calendar.calendar(year))

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

display_month_calendar(year, month)
display_year_calendar(year)
