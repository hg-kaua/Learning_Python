def count_sheep(n):
    # your code
    result = ""
    if n > 0:
        for i in range(1, n+1):
            result += f"{i} sheep..."   
        return result
    else:
        return ""

print(count_sheep(0))
print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))