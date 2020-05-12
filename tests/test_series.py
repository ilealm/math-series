from math_series import __version__

from math_series.series import fibonacci
# from math_series.series import fibonacci, lucas

def test_version():
    assert __version__ == '0.1.0'


def test_fibo_one():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibo_two():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibo_three():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_fibo_four():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected

def test_fibo_four():
    actual = fibonacci(14)
    expected = 377
    assert actual == expected
