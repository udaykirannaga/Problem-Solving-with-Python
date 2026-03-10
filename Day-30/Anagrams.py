'''
Write a python program to check if two strings are anagrams or not
What is anagrams
1. first string lenght equal or not, if equal
2. if we can form one string by arranging the characters 
of another string. For example, Race and Care.
'''

str1="Race"
str2="Care"
# so first i am converting the strings in 
#       lowercase becuse we can find easily
str1=str1.lower()
str2=str2.lower()

# check if length is same
if len(str1)==len(str2):
    
    # sort the strings
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)

    # if sorted char arrays are same
    if sorted_str1==sorted_str2:
        print(f"{str1} and {str2} both are anagrams")

# else conditon
else:
    print(f"{str1} and {str2} both are not anagrams")
