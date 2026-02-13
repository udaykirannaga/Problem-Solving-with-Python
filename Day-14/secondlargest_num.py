'''write python program to find second largest number'''
list_nums=[1,2,3,1,5,4,5]
largest=second_largest=float('-inf')
for num in list_nums:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print("second largest",second_largest)