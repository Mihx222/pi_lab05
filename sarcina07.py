def average(values):
    count = 0
    total = 0

    for value in values:
        if value is not None:
            total += value
        count += 1

    return total / count


values = [None, 4, 6, 8, 12, None, 56, 34, 123]
print(average(values))
