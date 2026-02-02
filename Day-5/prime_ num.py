'''
write python program to check prime number
prime numbers are positive integers thats greater than 1 that also have no 
    other factors 1 and number itself
    for example 6 which is divisible by 1 ,2,3,6 not prime
'''

def check_prime(number):
    # Check if the number is greater than 1
    # (prime numbers must be greater than 1)
    if number > 1:
        
        # Loop from 2 to number-1 to check divisibility
        for num in range(2, number):
            
            # If number is divisible by any num,
            # it is not a prime number
            if number % num == 0:
                return "Not a prime Number"
        
        # If no divisors are found, the number is prime
        return "prime"
    
    # If number is 1 or less, it is not a prime number
    return "Not a prime Number"
# From user
n=int(input("Enter a number to check prime or Not :"))
# Calling the function with -2
print(check_prime(n))

        