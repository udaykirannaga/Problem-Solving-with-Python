'''
write a python program to remove duplicates
'''

nums=[1,2,3,45,6,3,4,2,5,6,7,8,9]
unique=[]
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)


# method 2
lists=[1,2,3,1,2,3,1,2,3]
print(list(set(lists)))