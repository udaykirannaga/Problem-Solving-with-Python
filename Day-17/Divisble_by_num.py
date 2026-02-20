'''
Check if a number is divisible by 5 and 11.
'''
# num = int(input("Enter a number: "))

# if num % 5 == 0 and num % 11 == 0:
#     print("Divisible by both 5 and 11")
# elif num % 5 == 0:
#     print("Divisible only by 5")
# elif num % 11 == 0:
#     print("Divisible only by 11")
# else:
#     print("Not divisible by 5 or 11")


# using function
def divisible(num):
    if num % 5 == 0 and num % 11 == 0:
        print("Divisible by both 5 and 11")
    elif num % 5 == 0:
        print("Divisible only by 5")
    elif num % 11 == 0:
        print("Divisible only by 11")
    else:
        print("Not divisible by 5 or 11")
number = int(input("Enter a number: "))
divisible(number)