"""
Python program to check leap year
leap year:
A year is called leap year if it is contains additional day which makes 
    the number of days in that year is 366. This additonal day is added in the february 
    which make it 29 days long.
A leap year occured once every 4 years

How to determine if a year is leap year or not
following steps
if a year is evenly divisible by 4 means having no remainder then
    go to the next step. if it not divisible by 4 it is not a leap year
    for example 2001
If a year is divisible by 4, but not divisible by 100 
    If divisible by both 4 and 100, then go to next step
If a year divisible 100, but not divisible by 400, then it is 
    not a leap year

"""
# This function checks whether a given year is a leap year
def check_leap_year(year):
    # A year is a leap year if:
    # 1. It is divisible by 4 AND not divisible by 100
    # OR
    # 2. It is divisible by 400
    # The expression below returns True if the year is a leap year, otherwise False
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


# Taking input from the user
# input() always returns a string, so we convert it to an integer using int()
input_year = int(input("Input from the user : "))


# Calling the check_leap_year() function and checking the result
# If the function returns True, the year is a leap year
if check_leap_year(input_year):
    # This line executes if the condition is True
    print(f"It is a leap year {input_year}")
else:
    # This line executes if the condition is False
    print(f"Not a leap year {input_year}")


