"""
Validates strings as palindromes.
"""
from collections import deque
def is_palindrome(input_string):
    if (not isinstance(input_string, str)):
        raise ValueError("Wrong data type, must be a string")
    lower_string = str.lower(input_string)
    lower_space_string = lower_string.replace(" ","")
    deq_input = deque(lower_space_string)
    reverse_deq_input = deque(reversed(deq_input))
    if deq_input == reverse_deq_input:
        return deq_input == reverse_deq_input
    else:
        return False

