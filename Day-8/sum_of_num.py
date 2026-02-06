'''
Sum of all numbers in list
Write python function to sum of all numbers in list
nums=[1,2,4,5,6,2]


'''
# without function
numbers=[1,2,3,4,5]
total_sum=0
for nums in numbers:
    total_sum=total_sum+nums
print(total_sum)


# with function

def sum_of_nums(n):
    # This variable will store the total sum of numbers
    total_sum = 0

    # Loop through each number in the list n
    for num in n:
        # Add each number to total_sum
        total_sum += num

    # Return the final sum
    return total_sum


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Call the function and print the result
print(sum_of_nums(numbers))

