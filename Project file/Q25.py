from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.today()
    birth_date = datetime(birth_year, birth_month, birth_day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

age = calculate_age(birth_year, birth_month, birth_day)
print("Your age is:", age)
