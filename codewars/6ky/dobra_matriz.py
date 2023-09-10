def fold_array(array, runs):
    i = 0
    new_arr = []
    while i < runs:
        if len(array) > 1:
            new_arr = []    
            while len(array) > 1:
                new_arr.append(array[0]+array[-1])
                array = array[1:-1]
                
                if len(array) == 1:
                    new_arr.append(array[0])
        else:
            return array
        array = new_arr
        i += 1

    return new_arr

print(fold_array([1, 2, 3, 4, 5], 1))
print(fold_array([2], 10))
print(fold_array([1, 2, 3, 4, 5], 2))
print(fold_array([-36, 100, 50, -190, 27, -103, 40], 1))
print(fold_array([-36, 100, 50, -190, 27, -103, 40], 2))
print(fold_array([-36, 100, 50, -190, 27, -103, 40], 3))
print(fold_array([-36, 100, 50, -190, 27, -103, 40], 4))

# versao otimizada

def fold_array_otimizado(array, runs):
    mid = len(array) // 2
    print(reversed(array[mid:]))
    
    a = [sum(pair) for pair in zip(array[:mid] + [0], reversed(array[mid:]))]
    return fold_array(a, runs - 1) if runs > 1 else a

print(fold_array_otimizado([1, 2, 3, 4, 5], 1))

# mid = len(array) // 2: Isso calcula o índice do meio do array de entrada e armazena em mid. Isso é usado para dividir o array em duas partes iguais.

# a = [sum(pair) for pair in zip(array[:mid] + [0], reversed(array[mid:]))]: Nesta linha, a operação de dobramento é realizada. Isso é feito da seguinte maneira:

# array[:mid] pega a primeira metade do array.
# [0] é adicionado ao final da primeira metade. Isso é feito para garantir que a operação de dobramento funcione corretamente, mesmo se o comprimento do array for ímpar. Se o comprimento do array for ímpar, a soma final seria feita com zero.
# reversed(array[mid:]) inverte a segunda metade do array.
# zip(array[:mid] + [0], reversed(array[mid:])) cria pares de elementos, onde o primeiro elemento é da primeira metade com um zero no final, e o segundo elemento é da segunda metade invertida.
# Então, sum(pair) calcula a soma de cada par de elementos e cria uma nova lista a contendo essas somas.

# return fold_array(a, runs - 1) if runs > 1 else a: Esta é a parte recursiva da função. Se o número de "runs" (runs) for maior do que 1, a função chama a si mesma (fold_array) com a lista modificada a e decrementa o número de "runs" em 1. Isso repete o processo de dobramento na lista a para a quantidade de vezes especificada por runs. A recursão continua até que runs seja igual a 1, momento em que a função retorna o array final resultante.

# Espero que isso ajude a esclarecer como o código funciona!





