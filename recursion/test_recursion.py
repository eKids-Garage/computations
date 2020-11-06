import pytest

import palindrome
import prime_number
import sum_of_digits
import power_of_two

def test_palindrome():
    assert palindrome.is_palindrome("ELLE") == 'YES'
    assert palindrome.is_palindrome("ELDLE") == 'YES'
    assert palindrome.is_palindrome("ELDE") == 'NO'
    assert palindrome.is_palindrome("EDLE") == 'NO'
    assert palindrome.is_palindrome("ELDDLE") == 'YES'    
    assert palindrome.is_palindrome("TETS") == 'NO'


def test_prime():
    assert prime_number.is_prime(3557) == 'YES'
    assert prime_number.is_prime(139) == 'YES'
    assert prime_number.is_prime(2971) == 'YES'
    assert prime_number.is_prime(3556) == 'NO'
    assert prime_number.is_prime(6) == 'NO'


def test_sum_of_digits():
    assert sum_of_digits.sum(123) == 6
    assert sum_of_digits.sum(157) == 13
    assert sum_of_digits.sum(878) == 23
    assert sum_of_digits.sum(4545) == 18
    assert sum_of_digits.sum(2223) == 9

def test_power_of_two():
    assert power_of_two.is_power_of_two(2048) == 'YES'
    assert power_of_two.is_power_of_two(1024) == 'YES'
    assert power_of_two.is_power_of_two(4096) == 'YES'
    assert power_of_two.is_power_of_two(2) == 'YES'
    assert power_of_two.is_power_of_two(1) == 'YES'
    assert power_of_two.is_power_of_two(22222) == 'NO'
    assert power_of_two.is_power_of_two(6) == 'NO'
