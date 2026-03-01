'''
write python program for simple interest

S.I formula:
s.i=pxrxt/100
p=principle amount
r=rate of interest
t=time(in years)
'''

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time in years: "))

SI=P * R * T/100
print("simple Interest :",SI)