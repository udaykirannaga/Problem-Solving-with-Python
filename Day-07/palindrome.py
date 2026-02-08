'''
Write python program to check given number or string is palnidrome or not
input: MOM,radar,noon,121 
output: MOM,radar,noon,121
'''
# By using normal condtional 
is_palindrome="momy"
if is_palindrome==is_palindrome[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

# by using functions
# This function checks whether the given value is a palindrome
def is_palindrome(value):
    # value[::-1] reverses the string
    # We compare the original value with its reversed version
    return value == value[::-1]

# Take input from the user
user_input = input("Enter your palindrome to check if it is palindrome or not: ")

# Call the function and store the result (True or False)
result = is_palindrome(user_input)

# If result is True, it means the input is a palindrome
if result:
    print(f"It is a palindrome: {user_input}")
else:
    # If result is False, it is not a palindrome
    print(f"Not a palindrome: {user_input}")
