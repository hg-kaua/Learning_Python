def two_sum(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i != j:         
                if numbers[i] + numbers[j] == target:
                    tupla = (i, j)
                    return tupla
 
                
                
print(two_sum([1,2,3],4))
print(two_sum([2,2,3],4))