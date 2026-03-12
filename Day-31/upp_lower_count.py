'''
write a python program to count
upper case letters
lower case letters
'''
text="Uday Kiran Naga"
upper_case=0
Lower_case=0
for i in text:
    if i.isupper():
        upper_case+=1
    elif i.islower():
        Lower_case+=1
# Step 4: Print results
print("Uppercase letters:", upper_case)
print("Lowercase letters:", Lower_case)