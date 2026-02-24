# Function to calculate the nth Fibonacci number using recursion
def fibonacci(n):
    # Base case: if n is 0 or 1, return n directly
    # Fibonacci(0) = 0
    # Fibonacci(1) = 1
    if n <= 1:
        return n
    
    # Recursive case:
    # Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)


# Example usage:
# Print the first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")