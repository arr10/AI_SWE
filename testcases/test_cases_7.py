def test1():
    input_str = "Hello, World!"
    assert random_string_function(input_str) == "hELLO, wORLD!"

def test2():
    input_str = "Python 3.9"
    assert random_string_function(input_str) == "pYTHON 3.9"

def test3():
    input_str = "AbCdEfG 123"
    assert random_string_function(input_str) == "aBcDeFg 123"