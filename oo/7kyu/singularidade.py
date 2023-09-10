def real_numbers(n):
    count = sum(1 for i in range(1, n+1) if all(i % x != 0 for x in [2, 3, 5]))
    return count
    pass

print(real_numbers(5))
print(real_numbers(10))
print(real_numbers(20))
print(real_numbers(30))
print(real_numbers(100))


