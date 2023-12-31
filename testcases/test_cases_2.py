def test_cases_2():
    matrix1 = [[697, 100, 666, 773, 477], 
               [961, 359, 705, 21, 212], 
               [108, 739, 969, 220, 316], 
               [162, 962, 148, 493, 42], 
               [270, 599, 106, 199, 138], 
               [29, 184, 575, 701, 256]]

    matrix2 = [[413, 202], [526, 450]]
    
    expected_result = 0
    
    assert  buggy_2(matrix1, matrix2) == expected_result
        
    matrix1 = [[407, 711, 257, 30, 874], 
               [596, 449, 807, 592, 175], 
               [929, 776, 638, 565, 69], 
               [325, 455, 958, 642, 396], 
               [505, 13, 190, 373, 376], 
               [676, 382, 531, 240, 638], 
               [965, 680, 191, 554, 811]]

    matrix2 = [[202, 181, 154, 871, 470, 906, 572], 
               [91, 879, 291, 65, 86, 177, 435], 
               [592, 120, 568, 340, 9, 653, 123],                
               [444, 474, 833, 672, 857, 596, 168], 
               [432, 544, 189, 585, 887, 107, 260]]
    
    expected_result = [[689947, 1219152, 605731, 1019542, 1055697, 773808, 805980], 
                       [977443, 975195, 1207030, 1322880, 988566, 1517977, 780444], 
                       [916638, 1232159, 1214952, 1496564, 1054516, 1739763, 1060282], 
                       [1130311, 1093462, 1336229, 1301454, 1101948, 1425563, 712475], 
                       [543717, 506978, 571246, 975916, 893351, 846441, 478309], 
                       [867842, 982686, 837376, 1328676, 1126937, 1238119, 824355], 
                       [966210, 1499085, 1069739, 1796378, 1707884, 1536334, 1175205]]
    
    assert  buggy_2(matrix1, matrix2) == expected_result
    
    matrix1 = [[0, 3], [2, 4], [5, 10], [4, 4], [1, 1], 
                [4, 2], [1, 8], [3, 7], [9, 7], [9, 1]] 


    matrix2 = [[1, 3, 7, 8, 10, 5], 
                [0, 5, 2, 10, 1, 6]]

    expected_result = [[0, 15, 6, 30, 3, 18], 
                        [2, 26, 22, 56, 24, 34], 
                        [5, 65, 55, 140, 60, 85], 
                        [4, 32, 36, 72, 44, 44], 
                        [1, 8, 9, 18, 11, 11], 
                        [4, 22, 32, 52, 42, 32], 
                        [1, 43, 23, 88, 18, 53], 
                        [3, 44, 35, 94, 37, 57], 
                        [9, 62, 77, 142, 97, 87], 
                        [9, 32, 65, 82, 91, 51]]

    assert  buggy_2(matrix1, matrix2) == expected_result
    
test_cases_2()