def test1():
    some_list = ["apple", "banana", "orange", "grape", "kiwi"]
    assert add_to_list("watermelon", some_list) == some_list = ["apple", "banana", "orange", "grape", "kiwi", "watermelon"]
    
def test2():
    some_list = [42, 3.14, 7, 9.8, 1001]
    assert add_to_list(223) == [223]
    
def test3():
    some_list = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}, {"key4": "value4"}]
    assert add_to_list({"key4": "value4"}) == [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}, {"key4": "value4"}]