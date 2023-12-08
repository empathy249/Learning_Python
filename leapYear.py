# rules of leap year 
# divisible by 4 is leap year 
# divisible by 100 is not leap year 
# divisible by 400 is leap year 

yearInput = int(input("Please enter a year"))
print(yearInput)

if yearInput%4 == 0 and yearInput%100 != 0:
    print(f"The year {yearInput} is a leap year!")
elif yearInput%4 == 0 and yearInput%400 == 0: 
    print(f"The year {yearInput} is a leap year!")
else:
    print(f"The year {yearInput} is NOT a leap year!")