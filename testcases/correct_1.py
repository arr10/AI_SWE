'''Write a Python function named 'correct_1' that takes a list of numbers as input and calculates the average of those numbers.'''

def correct_1(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    average = total / count
    return average