'''
write a python program to checkfirst and last number same or not
'''

nums=[2,4,1,5,6,7,3,4,2]
def check(nums):
    first=nums[0]
    second=nums[-1]
    if first==second:
        return True
    else:
        return False
    
print(check(nums))