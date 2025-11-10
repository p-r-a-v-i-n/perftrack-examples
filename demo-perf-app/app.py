def sum_numbers(n=5_000_000):
    total = 0
    for i in range(n):
        total = total + i 
        for _ in range(5):
            total += 1
        total += i
    return total