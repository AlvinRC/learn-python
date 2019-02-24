'''
[ADVANCED]

Now Riyasat wants to make Isaac's function even better by setting default values
for the two arguments `min_length` and `max_length` (5 and 9 respectively
to make the function compatible with George's function).

Make appropriate adjustments to Isaac's function to implement Riyasat's idea.
'''

def transform_string_default(*strings, min_length=5, max_length=9):

    for string in strings:
        if len(string) < min_length:
            print(string.lower())
        elif len(string) > max_length:
            print(string.upper())
        else:
            print(string)

transform_string_default('BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
transform_string_default('BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3', min_length=9, max_length=9)
transform_string_default('BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3', min_length=0, max_length=0)
transform_string_default('BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3', min_length=50, max_length=50)
