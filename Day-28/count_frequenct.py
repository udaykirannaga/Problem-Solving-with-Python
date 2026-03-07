'''
write a python program to count frquncy of numbers
'''

my_list=[1, 2, 2, 3, 1, 4, 2, 3]
freq={}
for item in my_list:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)