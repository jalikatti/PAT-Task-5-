# Define a lambda function to generate Fibonacci series up to n elements
fib_series = lambda n: [fib(i) for i in range(n)]

# Define a lambda function to calculate the nth Fibonacci number recursively
fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)

# Generate Fibonacci series with 50 elements
fibonacci_50 = fib_series(50)

# Print the Fibonacci series
print(fibonacci_50)
