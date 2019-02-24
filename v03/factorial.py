
'''
Write a function that computes the factorial of a given number `n`.
You may assume that `n` is non-negative. (Note: 0! == 1)

If `n` is not specified, then it should compute the factorial of 5
'''

# Solution 1: iterative method
def factorial(n = 5):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Solution 2: recursive method
def factorial_2(n = 5):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n - 1)

# Solution 3: one-liner using lambda expression
factorial_3 = lambda n=5: 1 if n == 0 else n * factorial_3(n - 1)