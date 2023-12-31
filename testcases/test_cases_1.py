def test_cases_1():
    numbers = [2, 4, 6, 8, 10]
    assert buggy_1(numbers) == 6.0

    numbers = [7, -9, -10, -5, 10, -7, 4, 2, -6, -3, 5, 10, -4, 8, 0, -9, -10, -4, -1, -7]
    assert buggy_1(numbers) == -1.45

    numbers = [-6, -9, 10, -8, 6, -8, 0, -2, -2, 10, 3, -10, 8, -6, 10, 8, 9, -10, -4, -10, -6, -4,
               0, -8, 1, -3, 8, -4, -3, 9, 8, -8, -4, 0, 2, -10, 10, -6, -1, 6, 2, 3, 9, 3, -2, -9,
               -4, 9, 10, -7, -2, -5, 9, -4, -5, -8, -8, 10, -2, 0, 3, 9, 5, 10, 0, 4, -8, -8, -4,
               3, 3, -10, -2, 9, 10, 6, -5, -4, 6, 10, -5, 0, 3, -3, -6, 5, 5, 1, -7, 2, -1, -10,
               -10, -1, 7, -10, 5, -8, 9, 9]
    assert buggy_1(numbers) == -0.03

test_cases_1()
