def fibonacci(n):
    """Returns the integer value of n position in the fibonacci sequence."""
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
