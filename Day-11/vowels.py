'''
Write python program to check How many vowels present in string 
vowels="aeiouAEIOU"

'''
# Ask the user to enter their name or any string
user_input = input("Enter your name to check vowels: ")

# Define a string containing all lowercase vowels
vowels = "aeiou"

# Initialize a counter to keep track of the number of vowels
count = 0

# Convert the input to lowercase and loop through each character
for char in user_input.lower():
    # Check if the character is a vowel
    if char in vowels:
        # If yes, increase the count by 1
        count += 1  # same as count = count + 1

# Print the total number of vowels found in the input
print("Total vowels in given string:", count)
