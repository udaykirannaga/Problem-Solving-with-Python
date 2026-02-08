'''
Write Python program to check a given number is 
postive
Negative
zero
'''
# Taking a number from the user to check 
user_number=float(input("Enter a number:"))
if user_number>0:
    print(f"{user_number} is a Positive number")
elif user_number<0:
        print(f"{user_number} is a Negative number")
else:
        print(f"{user_number} is a Zero")

