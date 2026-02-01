'''
Largest Among Three numbers
'''
a=int(input("Input from user num1 :"))
b=int(input("Input from user num2 :"))
c=int(input("Input from user num3 :"))
# checking condition
if a>b and a>c:
    print("a is largest {a}")
elif b>a and b>c:
    print(f"b is largest {b}")
else:
    print(f"C is largest {c}")



# List of numbers to find the largest
list_nums = [25, 4, 20, 34, 15, 24, 4, 8, 9, 45]

# Assume the first number is the largest initially
largest = list_nums[0]

# Loop through the rest of the numbers in the list
for nums in list_nums[1:]:
    # If the current number is greater than 'largest'
    if nums > largest:
        # Update 'largest' with the current number
        largest = nums

# After the loop ends, 'largest' contains the maximum number
print(largest)


# you can also use python built-in function
print(max(list_nums))



