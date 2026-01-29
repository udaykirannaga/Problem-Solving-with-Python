"""
Check the input number is even or odd number
A number is even if divison by 2 gives a remainder 0
if the remainder is 1 it is odd
"""

user_input=int(input("Enter a number:"))
if user_input%2==0:
    print(f"{user_input} is a Even number")
else:
    print(f"{user_input} is a odd number")