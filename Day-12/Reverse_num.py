'''
write python program to reverse a number
example:
12345
54321
'''
num=12345
string=str(num)[::-1]
print(string)

# Without  methods
# Original number we want to reverse
number = 12345

# Variable to store the reversed number, starts at 0
reversed_number = 0

# Loop until the number becomes 0
while number > 0:
    # Get the last digit of the number
    digit = number % 10
    
    # Add the last digit to reversed_number
    # Shift previous digits left by multiplying by 10
    reversed_number = reversed_number * 10 + digit
    
    # Remove the last digit from number
    number = number // 10

# Print the reversed number
print(reversed_number)

    # 0*10+5=5
    # 5*10+4=54
    # 54*10+3=543
    #543*10+2=5432
    #5432*10+1=54321
