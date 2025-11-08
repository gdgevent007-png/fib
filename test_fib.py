# tests/test_fib.py
from fibonacci import fib

def test_values():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(7) == 13
    assert fib(8) == 21
