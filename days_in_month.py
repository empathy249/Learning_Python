
def is_leap_year(year): 
    leap_year = False
    if year % 4 == 0 and year % 400 == 0: 
        leap_year = True
    elif year % 4 == 0 and year % 100 != 0: 
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    else: 
        leap_year = False
    return leap_year


year_user = int(input("Please enter year: "))
month_user = int(input("Please enter month: "))
days_in_month = 0 

leap_year = is_leap_year(year_user)

if month_user == 1 or month_user == 3 or month_user == 5 or month_user == 7 or month_user == 8 or month_user == 10 or month_user == 12:
    days_in_month = 31
elif month_user == 4 or month_user == 6 or month_user == 9 or month_user == 11:
    days_in_month = 30
elif month_user == 2: 
    if leap_year == True: 
        days_in_month = 29
    else:
        days_in_month = 28
else: 
    print ("Please only enter valid months as numbers")

print (f"{month_user} in {year_user} has {days_in_month} days")
