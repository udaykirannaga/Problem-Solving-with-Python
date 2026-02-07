'''
Write python program to add two different lists using map and lambda
'''
# Write a Python program to add two different lists using map() and lambda

# First list of numbers
List_one = [1, 2, 3, 4]

# Second list of numbers
list_two = [5, 6, 7, 8]

# map() applies the lambda function to each pair of elements from both lists
# lambda a, b: a + b adds elements from List_one and list_two one by one
Result = list(map(lambda a, b: a + b, List_one, list_two))

# Print the final added list
print(Result)

# Output: [6, 8, 10, 12]

