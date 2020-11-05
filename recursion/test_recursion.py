import pytest

import palindrome
import prime_number
import sum_of_digits
import power_of_two

def test_is_palindrome():
    assert palindrome.is_palindrome("ELLE") == 'YES'

def test_is_not_palindrome():
    assert palindrome.is_palindrome("TETS") == 'NO'

def test_is_prime():
    assert prime_number.is_prime(3557) == 'YES'

def test_is_not_prime():
    assert prime_number.is_prime(3556) == 'NO'

def test_sum_of_digits():
    assert sum_of_digits.sum(123) == 6

def test_is_power_of_two():
    assert power_of_two.is_power_of_two(2048) == 'YES'



