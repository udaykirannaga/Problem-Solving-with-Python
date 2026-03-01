'''
write python program for compound interest
formula:
C.I=P(1+r/100)**t-P
p=priciple amount
'''

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time in years: "))

Amount = P * (1 + R/100) ** T
CI = Amount - P

print("Compound Interest is:", CI)
print("Total Amount is:", Amount)