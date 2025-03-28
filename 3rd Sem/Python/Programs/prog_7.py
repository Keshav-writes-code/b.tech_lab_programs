# Fibonacci Function using Recursion

print("A Program to get the Fibonacci number from a Value")
def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Assign a value to n
n = int(input("\nEnter a Value: "))

# Print the result
print(f"\nThe {n}th Fibonacci number is: {fibonacci(n)}")
