'''
Write a python program to detect the number of local variables declared 
    in the function

Local var: which declare inside a function
Global var: Which declares outside func and use throughout the programme
'''
abc="global variable"
def check_loc():
    a=10
    name="uday"
    condition=True
    #__code__ it is a constructor
print(check_loc.__code__.co_nlocals)