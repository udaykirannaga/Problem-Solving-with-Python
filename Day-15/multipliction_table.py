''' Write python program to multiplication table'''
# Take input from the user and convert it to integer
number = int(input("Enter your number :"))

# Loop from 1 to 10
for i in range(1, 11):
    # Print multiplication table for the given number
    print(f"{number} x {i} = {number * i}")


# ------------------------------
# Pattern style multiplication
# ------------------------------

# Outer loop controls the first number (1 to 10)
for i in range(1, 11):

    # Inner loop controls the second number (1 to 10)
    for j in range(1, 11):

        # Print multiplication of i and j
        print(i, "*", j, "=", i * j)