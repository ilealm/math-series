def fibonacci(n):
    """
    Returns the value of n in the fibonacci series.
    """
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


