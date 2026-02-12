'''
Write a python program to print half pyramid
'''
# Type 1
print("*")
print("* *")
print("* * *")
print("* * * *")

# Type 2
for i in range(1,5):
    print(i*" * ")

# Type 3

# Number of rows for the pattern
rows = 4  

# Outer loop controls the number of rows
for i in range(rows):
    
    # Inner loop controls the number of stars printed in each row
    # i+1 ensures stars increase row by row (1, 2, 3, 4...)
    for j in range(i + 1):
        print(" * ", end="")   # Prints star without moving to next line
    
    print()  # Moves to the next line after printing stars in current row

