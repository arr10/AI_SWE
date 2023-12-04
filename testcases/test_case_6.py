def test1():
    assert fibonacci_memoization(10) == 55


def test2():
    assert fibonacci_memoization(20) == 6752


def test3():
    assert fibonacci_memoization(7) == 13