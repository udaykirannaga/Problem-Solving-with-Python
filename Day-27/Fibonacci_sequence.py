'''
Write python program for fibonacci sequnce
'''
# creating function and passing paramneter n
def fibonacci(n):
    # initialize
    a=0
    b=1
    sum=0
    # checking conditions
    if n<0:
        print("Invalid input")
    # n==1
    elif n==1:
        print(a)
    # else condition
    else:
        print(a)
        print(b)
        # looping because to check number of times
        for i in range(2,n):
            # storing in another var
            c=a+b
            a=b
            b=c
            print(c)
fibonacci(5)