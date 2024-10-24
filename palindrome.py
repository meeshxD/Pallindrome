"""
Validates strings as palindromes.
"""
def is_palindrome(input_string):
    if (not isinstance(input_string, str)):
        raise ValueError("Wrong data type, must be a string")
    lower_string = str.lower(input_string)
    lower_space_string = lower_string.replace(" ","")
    reverse_input = lower_space_string[::-1]
    if lower_space_string == reverse_input:
        return lower_space_string == reverse_input
    else:
        return False