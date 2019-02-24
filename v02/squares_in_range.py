'''
Write a program that takes two numbers `a` and `b`,
and prints the square of every number between `a` and `b`
'''

# Solution 1: two for-loops, using reversed
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: "))

if a <= b:
    for n in range(a, b + 1):
        print(f'{n} * {n} = {n * n}')
else:
    for n in reversed(range(b, a + 1)):
        print(f'{n} * {n} = {n * n}')




# Solution 2: two for-loops, using step value
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: "))

if a <= b:
    for n in range(a, b + 1, 1):
        print(f'{n} * {n} = {n * n}')
else:
    for n in range(a, b - 1, -1):
        print(f'{n} * {n} = {n * n}')




# Solution 3: conditional step value
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: "))

step = 1 if a <= b else -1
for n in range(a, b + step, step):
    print(f'{n} * {n} = {n * n}')

