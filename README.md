# Learn Python
Watch the following videos on Python by Anna and do the exercises to become a Python master!

# Table of Contents
   * [1. Introduction to Python](#1-introduction-to-python)
   * [2. Syntax and Control Structure](#2-syntax-and-control-structure)
   * [3. Functions](#3-functions)
   * [4. Modules and Virtual Environments](#4-modules-and-virtual-environments)
   * [5. List Data Structure](#5-list-data-structure)
   * [6. More Data Structures](#6-more-data-structures)

<br/>

## How to use this tutorial
1. Go through the videos in order
2. Complete the exercises under each video
3. For simple questions, click "Solution" to reveal the answer
4. For more complicated coding exercises, the answers are provided as separate files in the repository. The recommended way is to clone the whole repo so that run, modify and experiment more with the solutions :)
5. This tutorial may get more updates in the future, so pull the repo regularly to ensure that your local copy is up-to-date
6. If you have any requests/suggestions or have spotted errors/typos please let me know through here: https://goo.gl/forms/GwgulRl1ZX2bwbht2

<br/>

**WARNING**: we have provided alternate solutions to some of the coding exercises below which use fewer lines of code. Although they may be fun little demonstrations of what python is capable of and its more advanced features, some of them are often very unreadable and you should NEVER code like that in practice!

<br/>

# 1. Introduction to Python
[1. Introduction to Python](https://www.youtube.com/watch?v=M5ts0NKmqOo)

### Types of Variables
The `type()` built-in function that tells you the data type of a given value or a variable
```python
print(type(3), type(3.14), type("Pi"), type('3.14'), type(True), type(False))
```

<br/>

###  Q1
What is the value of the variable `c`?

```python
c = str(10) + "123"
```


<details><summary>Solution</summary>

```python
"10123"
```
</details>

<br/>

### Q2
How would you add the following values as numbers?

```python
a = 3.14
b = "42.02"
```

<details><summary>Solution</summary>

```python
a + float(b)
```
</details>

<br/>

###   Q3
Given two numbers `a` and `b`, write a print statement that prints out the two variables in the following format: "`a` times `b` is `c`", where `c` is the product of the two numbers.

E.g., if `a=5` and `b=7`, your print statement should output
```
5 times 7 is 35
```


<details><summary>Solution</summary>

```python
print('{} times {} is {}'.format(a, b, a * b))
print(f'{a} times {b} is {a * b}')
```
</details>


<br/>

### BIG NUMBERS in Python
 Unlike in C or Java, in Python you can easily operate with very large numbers! Try running the following lines of code.
 
```python
print(f'There are about {10 ** 82} atoms in the world')
print(f'This can fill up your terminal with numbers: {12345  **  12345}')
```


<br/>
<br/>
<br/>


# 2. Syntax and Control Structure
[2. Syntax and Control Structure](https://www.youtube.com/watch?v=X8LInoE2lrQ)

### Q1 - [v02/number_guesser.py](https://github.com/apple25/learn-python/blob/master/v02/number_guesser.py)
Modify the number guesser from the above video to print out the number of times you guessed in total.


E.g.,
```
Enter a guess between 1 and 10
5
Guess was too low!
7
Guess was too low!
9
Guess was too high!
8
You got the correct answer in 4 guesses!
```

<br/>

### Q2 - [v02/descending_even.py](https://github.com/apple25/learn-python/blob/master/v02/descending_even.py)

Write a for loop that prints even numbers from 10 to 1, separated by newlines

I.e.,
```
10
8
6
4
2
```

<br/>


### Q3 - [v02/squares_in_range.py](https://github.com/apple25/learn-python/blob/master/v02/squares_in_range.py)

Write a program that takes two numbers `a` and `b`, then prints the square of every number from `a` to `b` inclusively.

E.g.,
```
Enter first number: -2
Enter secondnumber: 5
-2 * -2 = 4
-1 * -1 = 1
0 * 0 = 0
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
```

```
Enter first number: 3
Enter second number: -3
3 * 3 = 9
2 * 2 = 4
1 * 1 = 1
0 * 0 = 0
-1 * -1 = 1
-2 * -2 = 4
-3 * -3 = 9
```
<br/>

**HINT**: If you are stuck, try solving the problem for when `a <= b` and when `a > b` separately, then combine the two solutions into one. 

<br/>

### Q4 - [v02/repeated_digit_addition.py](https://github.com/apple25/learn-python/blob/master/v02/repeated_digit_addition.py)

Write a program that accepts a single digit `a` from the user and computes the value of `a + aa + aaa`

For example, if `a = 7`, then the output should be `861`, which is equal to `7 + 77 + 777`

You may assume that user input is always a single digit (i.e., in the range 0 to 9)


E.g.,
```
Enter a digit: 5
615
```

<br/>


**HINT:** There are many different ways to solve this problem, try...

1. String concatenation, i.e. string addition in Python
2. String formatting, e.g., `f'{variable}'`
3. Without using any string manipulations, that is, solve 


<br/>


### Q5 CHALLENGE! - [v02/repeated_digit_addition_adv.py](https://github.com/apple25/learn-python/blob/master/v02/repeated_digit_addition_adv.py)

Write a program that accepts a single digit `a` from the user and computes the sum `a + aa + aaa + ...` where the number of terms in the sum is equal to `a`

For example,
- if `a = 1`, then sum is `1`
- if `a = 2`, then sum is `2 + 22 = 24`
- if `a = 3`, then sum is `3 + 33 + 333 = 369`

and so on ...

E.g.,
```
Enter a digit: 5
61725
```

*Note: what should the output be for* `a = 0` *?*



<br/>
<br/>
<br/>


# 3. Functions
[3. Functions](https://www.youtube.com/watch?v=TqA_kg6nhyo)


### Adding an Arbitrary number of Numbers
Here is the function that was provided in the video above.
```python
def add_numbers(*numbers):
	total =  0
	for number in numbers:
		total += number
	return total
```

What are the outputs of the following print statements?

<details><summary>Solution</summary>

```python
>> print(add_numbers(5, 10, 4))
19
>> print(add_numbers())
0
```
</details>
 
 *You can simplify the above function by using the built-in function* `sum()` *as below*
```python
def add_numbers(*numbers):
	return sum(numbers)
``` 

*Or simply use the built-in function, without re-inventing the wheel!*
```python
# Notice the extra pair of parentheses surrounding the input to the function - we will learn about why we need them later
print(sum((5, 10, 4)))
print(sum(())
```

<br/>

### Flexible Arguments
Can a function declare two flexible arguments? Why or why not?



<br/>

### Q1 - [v03/factorial.py](https://github.com/apple25/learn-python/blob/master/v03/factorial.py)

Write a function that computes the factorial of a given integer `n`. You may assume that `n` is non-negative. *(Note: 0! = 1)*

If `n` is not specified, then it should compute the factorial of 5.

E.g.,
```python
>> print(factorial(4))
24
>> print(factorial())
120
```

<br/>

### Q2 - [v03/perfect_match.py](https://github.com/apple25/learn-python/blob/master/v03/perfect_match.py)

Two numbers `a` and `b` are said to be a perfect match if their sum is dividisble by some given integer `k`. Write a function that accepts three arguments `k, a, b` and returns `True` if `a` and `b` form a perfect match, `False` otherwise.

If the value of `k` is not provided, then it should default to 10.

Note that `k` may be negative, positive or zero; but in the case that `k = 0`, the function should always return `False`

**Hints**: 
- `x % y` returns the remainder of `x` divided by `y`
- Try to vary the order of the three arguments in the function declaration - what do you notice?


E.g.,
```python
>> print(is_perfect_match(13, 7))
True
>> print(is_perfect_match(1, -11))
True
>> print(is_perfect_match(5, -5))
True
>> print(is_perfect_match(3, 5))
False
>> print(is_perfect_match(3, 5, 4))
True
>> print(is_perfect_match(3, 6, 4))
False
>> print(is_perfect_match(3, 5, -4))
True
>> print(is_perfect_match(3, 5, 0))
False
```

<br/>



### Q3 - [v03/transform_string.py](https://github.com/apple25/learn-python/blob/master/v03/transform_string.py)

George wishes to write a function called `transform_string` that takes in any number of string arguments and prints out each string after applying the following transformation:

1. shorter than **5** characters: every letter in the string is converted to lowercase
2. between **5** to **9** characters (inclusive): no change
3. longer than **9** characters: every letter in the string is converted to uppercase

Write the function for George.

E.g.,
```python
>> transform_string('BIGG', 'camelCase', '_snake_case_', '', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
bigg
camelCase
_SNAKE_CASE_

SOFTWAR3 ENGINEER1NG
hi3
```

**Hints**:
1. Use the built-in function `lower()` to convert a string into lowercase. E.g.,
	```python
	>> print('HeLLo World!'.lower())
	hello world!
	```
2. `len(string)` gives the length of the string
	```python
	>> print(len('hi!'))
	3
	```
<br/>



### Q4 - [v03/transform_string_min_max.py](https://github.com/apple25/learn-python/blob/master/v03/transform_string_min_max.py)

Isaac wants to upgrade George's function to take in two extra integer arguments `min_length` and `max_length` that would replace the values 5 and 9 from the original function respectively.

You may assume that `min_length` is always less than or equal to `max_length`

Modify the function from the above exercise to make Isaac happy.

E.g.,
```python
>> transform_string_min_max(5, 9, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
bigg
camelCase
_SNAKE_CASE_
SOFTWAR3 ENGINEER1NG
hi3
>> transform_string_min_max(9, 9, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
bigg
camelCase
_SNAKE_CASE_
SOFTWAR3 ENGINEER1NG
hi3
>> transform_string_min_max(0, 0, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
BIGG
CAMELCASE
_SNAKE_CASE_
SOFTWAR3 ENGINEER1NG
HI3
>> transform_string_min_max(50, 50, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
bigg
camelcase
_snake_case_
softwar3 engineer1ng
hi3
```

<br/>


### Q5 CHALLENGE! - [v03/transform_string_default.py](https://github.com/apple25/learn-python/blob/master/v03/transform_string_default.py)

Now Riyasat wants to make Isaac's function even better by setting default values for the two arguments `min_length` and `max_length` (5 and 9 respectively to make it compatible with George's function).

Make appropriate adjustments to Isaac's function to implement Riyasat's idea.

**Note**: this exercise is very difficult and requires knowledge of Python aside from what has been covered so far. So feel free to search for hints online or check the answers if you feel stuck for too long.

**Hint**: calling this function will require a different method of specifying the arguments.

<br/>



### Higher Order Functions
In Python, functions can be treated almost like any other variables. You can...
1. Pass in functions as arguments of another function
2. Return a function as an output of another function
3. Declare functions inside functions!

Here's an example of a function that does all of those:

```python
def my_decorator(func):
	def wrapper():
		print('This is printed before the function is called')
		func()
		print('This is printed after the function is called')
	return wrapper
```
`my_decorator` accepts a function `func` as an argument and returns a new function that has extra behaviour added on top of `func`; the returned function will print a line of text at the start of the function call and another line upon its completion. Functions like `my_decorator` are called as **decorators**.


More on high-order functions: https://www.hackerearth.com/practice/python/functional-programming/higher-order-functions-and-decorators/tutorial/

<br/>


### Lambda (Anonymous) Functions
You can also define one-line functions, using what's called the lambda expression. This is a convenient way for writing simple functions, and it should not be abused.

E.g.,
```python
# Regular way to define functions
def add1(x, y):
	return x + y

# Using a lambda expression
add2 = lambda x, y: x + y

# Both will output 7
print(add1(3, 4))
print(add2(3, 4))
```

Lambda functions are typically used when a simple function is required only once, often as an argument to a higher-order function. The example below uses the lambda function to conditionally filter a list of numbers (more on lists later).

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
even_numbers = list(filter(lambda x: (x % 2 == 0), numbers ))
```

<br/>
<br/>
<br/>


# 4. Modules and Virtual Environments
[4. Modules and Virtual Environments](https://www.youtube.com/watch?v=hc1sDvTjUo4)

### Setup
For this set of exercises, you are required to create three separate Python files: `circle.py`, `string_formatter.py` and `run.py`.

1. Create the files `string_formatter.py` and `run.py` under the same directory.
2. Create a subdirectory `shapes` under the same directory as the above two files
3. Create `circle.py` under the subdirectory `shapes`

<br/>


### Q1 - [v04/shapes/circle.py](https://github.com/apple25/learn-python/blob/master/v04/shapes/circle.py)

1. Write a function called `area` that accepts `radius` and returns the area of a circle with the given radius
2. Write a function called `circumference` that accepts `radius` and returns the circumference of a circle with the given radius
3. Define a variable `big_pie` and set its value to twice the value of `pi`

For the above tasks, you must import and use the value of `pi` that is defined in the [math library](https://docs.python.org/3/library/math.html). 

<br/>

### Q2 - [v04/string_formatter.py](https://github.com/apple25/learn-python/blob/master/v04/string_formatter.py)

Write a function called `prettify` which accepts two arguments `value` and `count`. It should convert `value` into a string and surround it with `~` on both sides of the string. The second argument, `count` should determine the number of `~` on each side, and it should default to 5 if not specified.

E.g.,:
```python
>> print(prettify(123))
~~~~~123~~~~~
>> print(prettify(1.4142, 2))
~~1.4142~~
>> print(prettify('hello!', 0))
hello!
```

<br/>

Paste the following print statements at the bottom of your file to test your function (also **required** for the next exercise)

```python
print(prettify(123))
print(prettify(1.4142, 2))
print(prettify('hello!', 0))
```

<br/>

### Q3 - [v04/run.py](https://github.com/apple25/learn-python/blob/master/v04/run.py)

In the file `run.py`, import from `circe.py` all of its functions and global variables. Next, import `prettify` from from `string_formatter.py`.

Under the import statements, paste the following lines of code to test the imported functions and variables:

```python
if __name__ == '__main__':
	r = int(input('Radius: '))

	area_str = prettify(area(r))
	circ_str = prettify(circumference(r), 3)
	bpie_str = prettify(big_pie, 7)

	print(f'Area: {area_str}')
	print(f'Circumference: {circ_str}')
	print(f'Big Pie: {bpie_str}')
```

What is the if statement for? We'll see what it does in a moment.

**Hint**: in Python, you can import from a relative path, say "directoryA/subdirectoryB/my_file.py", but replace all the slashes `/` with full stops `.`

<br/>

Now run `python3 run.py` to execute the program. What do you notice?

You should see something like this:
```
~~~~~123~~~~~
~~1.4142~~
hello!
Radius:
```

As you might have realised, the first three lines in the above output came from the print statements inside `string_formatter.py`  when the file was imported by `run.py`. 

If you want to prevent the print statements from running whenever the file is imported, you could simply delete them from your file. But sometimes, you might actually want to keep them within your file.  In that case, you can simply wrap your print statements under a special if statement like so:

```python
if __name__ == '__main__':
	print(prettify(123))
	print(prettify(1.4142, 2))
	print(prettify('hello!', 0))
```

Now try `python3 string_formatter.py` and `python3 run.py`. The print statements will execute when `string_formatter.py` is run directly as a script, but they will not exectue when the file is imported by another file.

But do `__name__` and `__main__` mean? For more information, read [this](https://www.geeksforgeeks.org/__name__-special-variable-python/)  or just look them up online.



<br/>
<br/>
<br/>




# 5. List Data Structure
[5. List Data Structure](https://www.youtube.com/watch?v=BXyEcdTtlm8)


-COMING SOON-


<br/>
<br/>
<br/>



# 6. More Data Structures
[6. More Data Structures](https://www.youtube.com/watch?v=DZss6668dQ0)

-COMING SOON-


<br/>
<br/>
<br/>
