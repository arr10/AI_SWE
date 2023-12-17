def test1():
    assert buggy_5("I am ", 5) == "I am 5"
    
def test2():
    assert buggy_5("I got ", 53) == "I got 53"
    
def test3():
    assert buggy_5("I need ", 12) == "I need 12"