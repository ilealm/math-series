from math_series import __version__

from math_series.series import fibonacci, lucas, sum_series

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

def test_fibo_five():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibo_six():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibo_seven():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_lucas_one():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_two():
    actual = lucas(10)
    expected = 123
    assert actual == expected

def test_lucas_three():
    actual = lucas(12)
    expected = 322
    assert actual == expected

def test_lucas_four():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_five():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_six():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_six():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def tesst_sum_series_one():
    # testing on fibonacci
    actual = sum_series(12)
    expected = 144
    assert actual == expected

def tesst_sum_series_two():
    # testing on lucas
    actual = sum_series(10,2,1)
    expected = 123
    assert actual == expected

def tesst_sum_series_three():
    # testing on custom sequence
    actual = sum_series(5,1,5)
    expected = 17
    assert actual == expected

def tesst_sum_series_four():
    # testing on custom sequence
    actual = sum_series(3,1,10)
    expected = 21
    assert actual == expected
