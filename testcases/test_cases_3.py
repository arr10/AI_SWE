def test_cases_3():
    some_list = ["apple", "banana", "orange", "grape", "kiwi"]
    assert buggy_3("watermelon", some_list) == some_list = ["apple", "banana", "orange", "grape", "kiwi", "watermelon"]
    
    some_list = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}, {"key4": "value4"}]
    assert buggy_3({"key4": "value4"}) == [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}, {"key4": "value4"}]
    
    some_list = [42, 3.14, 7, 9.8, 1001]
    assert buggy_3(223) == [223]
    
test_cases_3()