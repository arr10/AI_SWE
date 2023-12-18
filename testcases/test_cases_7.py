def test_cases_7():
    input_str = "Hello, World!"
    assert buggy_7(input_str) == "hELLO, wORLD!"

    input_str = "Python 3.9"
    assert buggy_7(input_str) == "pYTHON 3.9"

    input_str = "AbCdEfG 123"
    assert buggy_7(input_str) == "aBcDeFg 123"


test_cases_7()