def is_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True
    return False

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month <=12 and month>=1:
        if is_leap_year(year):
            month_days[1] = 29
        return f"There are {month_days[month - 1]} days in {month}th month of year {year}"
    else:
        return "Invalid Month"
    
print(days_in_month(year = int(input("Enter year: ")), month = int(input("Enter month number: "))))