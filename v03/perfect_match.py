'''
Two numbers `a` and `b` are said to be a perfect 
match if their sum is dividisble by some given number`k`

Write a function that accepts three arguments k, a, b
and returns True if `a` and `b` form a perfect match, False otherwise

If the value of `k` is not provided, then `k` should default to 10
'''

# Solution 1: readable version
def is_perfect_match(a, b, k=10):
    if k == 0:
        return False

    if (a + b) % k == 0:
        return True
    else:
        return False

# Solution 2: possibly less readable version
def is_perfect_match_2(a, b, k=10):
    return (k is not 0) and (a + b) % k == 0


print(is_perfect_match(13, 7))
print(is_perfect_match(1, -11))
print(is_perfect_match(5, -5))
print(is_perfect_match(3, 5))
print(is_perfect_match(3, 5, 4))
print(is_perfect_match(3, 6, 4))
print(is_perfect_match(3, 5, -4))
print(is_perfect_match(3, 5, 0))