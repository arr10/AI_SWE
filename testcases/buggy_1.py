def buggy_1(numbers):
    '''Write a Python function named 'buggy_1' that takes a list of numbers as input and calculates the average of those numbers.'''

    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1
        
        if count % 2 == 0:
            total += num

    average = total / count
    return average