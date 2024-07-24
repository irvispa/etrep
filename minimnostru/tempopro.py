# Python 2.x code
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            next_fib = fib[i-1] + fib[i-2]
            fib.append(next_fib)
        return fib[n-1]

# Test the function
print(fibonacci(10))  # Output: 34
