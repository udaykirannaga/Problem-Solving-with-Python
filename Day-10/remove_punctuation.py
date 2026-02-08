'''
Write python program to remove panctuations in string
panctuations are ''""@#$%^&*()!,.
'''
# List of punctuation marks we want to remove from the input
panctuations = "'',.!@#$%^&*()"

# Take input from the user
input_string = input("Input from the user: ")

# Initialize an empty string to store the result
new_string = ""

# Loop through each character in the input string
for char in input_string:
    # If the character is NOT in our punctuation list, add it to new_string
    if char not in panctuations:
        new_string += char

# Print the new string without the punctuation
print(new_string)
