'''
write a python program to count consonants in a given word
vowels=['a','e','i','o','u']
word=input("Enter you word to count consonants :")
count=0
for character in word:
    if character not in vowels:
        count+=1
print(count)

'''
# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Ask the user to enter a word
word = input("Enter your word to count consonants: ")

# Initialize a counter for consonants
count = 0

# Loop through each character in the word
for character in word:
    # If the character is NOT a vowel, it is a consonant
    if character.lower() not in vowels:  # .lower() ensures it works for uppercase letters too
        count += 1  # Increment the consonant counter

# Print the total number of consonants
print(count)
        