def test_cases_15():
    assert buggy_15([1,2,3,1]) == True
    assert buggy_15([1,2,3,4]) == False
    assert buggy_15([1,1,1,3,3,4,3,2,4,2]) == True

test_cases_15()