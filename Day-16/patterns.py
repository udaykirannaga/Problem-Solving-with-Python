''' 
write a python code print patterns


* * * *
* * * *
* * * *
* * * *
'''

for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()


'''
*
* *
* * *
* * * *

'''

print("half pyramid")
for i in range(1,5)    :
    print(i*"* ")
 # or

for i in range(1,5):
    for j in range(i):
        print("# ", end="")
    print()

'''
# Reverse half pyramid
* * * *
* * *
* *
*
'''

for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()

'''
1 2 3 4
2 3 4
3 4 
4

'''

n=4
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end=" ")
    print()    
