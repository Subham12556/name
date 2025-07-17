# Function to generate Fibonacci series
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Input: Number of terms in the Fibonacci series
num_terms = int(input("Enter the number of terms: "))

# Display the Fibonacci series
print(fibonacci(num_terms))

