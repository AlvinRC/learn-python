'''
Challenge!

Write a program that accepts a single digit `a` from the user and
computes the sum a + aa + aaa + ... where the number of terms in the
sum is equal to `a`

I.e.
    if a = 1, sum = 1,
    if a = 2, sum = 2 + 22 = 24,
    if a = 3, sum = 3 + 33 + 333 = 369,
    and so on

What should the output be for a = 0?
'''

# Solution 1: using string multiplication
a = input('Enter a digit: ')

total = 0
for n in range(1, int(a) + 1): # REPEAT FOR n = 1, ..., a
    total = total + int(a * n)

print(f'Total: {total}')




# Solution 2: using string concatenation
a = input('Enter a digit: ')

term = ''
total = 0
for _ in range(int(a)): # REPEAT `a` TIMES
    term = term + a
    total = total + int(term)

print(f'Total: {total}')




# Solution 3: multiply `a` with 1234...a, e.g. 1234567 if a = 7 (NOT recommended)
a = input('Enter a digit: ')

multiplier = '0' # multiplier = '' works too, except for a = 0 case
for n in range(1, int(a) + 1):
    multiplier = multiplier + str(n)

print(f'Total: {int(multiplier) * int(a)}') # note: int('012345') == 12345




# Solution 4: multiply `a` with 1234...a (version 2)
a = input('Enter a digit: ')
a = int(a)

multiplier = 0
for n in range(1, a + 1):
    multiplier = multiplier * 10 + n

print(f'Total: {multiplier * a}')




# Solution 5: three-liner (watch the following videos to understand it)
a = input('Enter a digit: ')
total = sum( int(a * n) for n in range(1, int(a) + 1) )
print(f'Total: {total}')




# Solution 6: one-liner (please don't do this)
(lambda a: (print(f'Total: {sum(  int(a * n) for n in range(1, int(a) + 1)  )}'))) (input('Enter a digit: '))