"""
Tests the palindrome module
"""
import pytest
from palindrome import is_palindrome
def test_string():
    with pytest.raises(ValueError, match="Wrong data type, must be a string"):
        is_palindrome(12321)