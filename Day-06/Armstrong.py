'''
check the number is the armstrong number or not
withour power function
armstrong:
A number which is equal to the sum of its digits raised by the 
    power of the number of the digits
'''
# Take a number from the user
n = int(input("Enter a number: "))

# Store the original number for comparison later
Dup = n

# Find how many digits are in the number
# Example: 153 → "153" → length = 3
length_num = len(str(n))

# Variable to store the sum of digits raised to power of number of digits
total_sum = 0

# Loop until all digits are processed
while n != 0:
    # Get the last digit of the number
    # Example: 153 % 10 = 3
    result = n % 10

    # Raise the digit to the power of total digits and add to total_sum
    # Example: 3^3 = 27
    total_sum += (result ** length_num)

    # Remove the last digit from the number
    # Example: 153 // 10 = 15
    n = n // 10

# Compare original number with calculated sum
if Dup == total_sum:
    print(f"It is {Dup} Armstrong number")
else:
    print(f"It is Not {Dup} Armstrong number")

