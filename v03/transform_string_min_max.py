'''
Isaac wants to upgrade George's function to take in two extra integer arguments
`min_length` and `max_length` that would replace the values 5 and 9 from the 
original function respectively.

Modify the function from the above exercise to make Isaac happy.

You may assume that min_length <= max_length
'''

def transform_string_min_max(min_length, max_length, *strings):

    for string in strings:
        if len(string) < min_length:
            string = string.lower()
        elif len(string) > max_length:
            string = string.upper()   
           
        print(string)

transform_string_min_max(5, 9, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
transform_string_min_max(9, 9, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
transform_string_min_max(0, 0, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
transform_string_min_max(50, 50, 'BIGG', 'camelCase', '_snake_case_', 'SoFtWaR3 EnGiNeEr1Ng', 'Hi3')
