'''
Write a for loop that prints even numbers from 10 to 1, separated by newline
'''

# Solution 1: using -1 step value
for i in range(10, 0, -2):
    print(i)

# Solution 2: using reversed
for i in reversed(range(2, 11, 2)):
    print(i)

# Solution 3: one-liner (NOT recommended)
print(*range(10, 0, -2), sep='\n')
