def correct_1(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    average = total / count
    return average