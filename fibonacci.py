# fibonacci.py

def fib(n):
    """
    Return nth Fibonacci number with:
      fib(0) = 0, fib(1) = 1
    Subtle bug present: incorrect loop bounds or base-case handling can introduce off-by-one.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    # correct loop: run n-1 steps to get fib(n)
    for _ in range(n - 1):
        a, b = b, a + b
    return b
