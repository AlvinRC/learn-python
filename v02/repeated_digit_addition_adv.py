'''
Write a program that accepts a single digit `a` from the user and
computes the value of a + aa + aaa

E.g. if a = 7, then the output should be 861, which is equal to 7 + 77 + 777

You may assume that user input is always a single digit

HINT: There are many different ways to solve this problem. Try...
 1. String concatenation, i.e. string addition in Python
 2. String formatting, e.g. f'{variable}'
 3. Without using any string manipulations, i.e. solve mathematically
'''

# Solution 1: using string concatenation
a = input('Enter a digit: ')
n1 = int(a)
n2 = int(a + a)
n3 = int(a + a + a)
print(n1 + n2 + n3)




# Solution 2: using string formatting
a = input('Enter a digit: ')
n1 = int(f'{a}')
n2 = int(f'{a}{a}')
n3 = int(f'{a}{a}{a}')
print(n1 + n2 + n3)




# Solution 3: using C-style string formatting
a = input('Enter a digit: ')
n1 = int( '%s' % a )
n2 = int( '%s%s' % (a, a) )
n3 = int( '%s%s%s' % (a, a, a) )
print(n1 + n2 + n3)




# Solution 4: using string multiplication
a = input('Enter a digit: ')
n1 = int(a)
n2 = int(a * 2)
n3 = int(a * 3)
print(n1 + n2 + n3)




# Solution 5: for mathematicians
a = int(input('Enter a digit: '))
print(1 * a + 11 * a + 111 * a)




# Solution 6: one-liner (NOT recommended since not readable)
print(123 * int(input('Enter a digit: ')))