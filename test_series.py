import pytest

from series import fibonacci
from series import lucas
from series import sum_series

def test_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_eleven():
    actual = fibonacci(11)
    expected = 89
    assert actual == expected

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_11():
    actual = lucas(11)
    expected = 199
    assert actual == expected

def test_sum_fib():
    actual = sum_series(7,0,1)
    expected = 13
    assert actual == expected
  
def test_sum_lucas():
    actual = sum_series(11,2,1)
    expected = 199
    assert actual == expected