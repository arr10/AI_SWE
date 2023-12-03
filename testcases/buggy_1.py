def calculate_average(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1
        
        if count % 2 == 0:
            total += num

    average = total / count
    return average