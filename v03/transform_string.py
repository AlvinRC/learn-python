'''
George wishes to write a function called `transform_string` that takes in
any number of string arguments and prints out each string after
applying the following transformation:

1. shorter than 5 characters: every letter in the string is converted to lowercase
2. between 5 to 9 characters (inclusive): no change
3. longer than 9 characters: every letter in the string is converted to uppercase

Write the function for George.
'''

# Solution 1: concise if statements
def transform_string(*strings):

    for string in strings:
        if len(string) < 5:
            print(string.lower())
        elif len(string) > 9:
            print(string.upper())
        else:
            print(string)


# Solution 2: alternative use of if statements
def transform_string_2(*strings):

    for string in strings:
        length = len(string)

        if length < 5:
            print(string.lower())
        elif 5 <= length and length <= 9:
            print(string)
        else:
            print(string.upper())


# Solution 3: single print statement
def transform_string_3(*strings):

    for string in strings:
        if len(string) < 5:
            string = string.lower()
        elif len(string) > 9:
            string = string.upper()   
           
        print(string)

transform_string('BIGG', 'camelCase', '_snake_case_', '', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')