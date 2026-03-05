'''
write a python program for counting number od occurances of a character
    in a string.


'''
word='programming'
character='g'
count=0
for i in word:
    if i==character:
        count+=1
print(count)