def test_cases_8():
    input_string = "hello"
    assert(buggy_8(input_string) == 'helloifmmp')

    input_string = 'Sunny day'
    assert(buggy_8(input_string) == 'Sunny day Tvooz!ebz!')

    input_string = 'timber-timber'
    assert(buggy_8(input_string) == 'timber-timber')


test_cases_8()