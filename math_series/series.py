def fibonacci(n):
    """Returns the integer value of n position in the fibonacci sequence."""
    if n == 0 : return 0
    if n == 1 : return 1
    left = 0
    right = 1
    i = 1
    sum_serie = 0
    while i <= (n-1):
        sum_serie = left + right
        left = right
        right = sum_serie
        i+=1

    return sum_serie


def lucas(n):
    """Returns the integer value of n position in the lucas sequence."""
    if n == 0 : return 2
    if n == 1 : return 1
    left = 2
    right = 1
    i = 1
    sum_serie = 0
    while i <= (n-1):
        sum_serie = left + right
        left = right
        right = sum_serie
        i+=1

    return sum_serie

print(lucas(7))
