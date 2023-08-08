def somaPar(lista):
    soma = 0
    for num in lista:
        if(num % 2 == 0):
            soma += num
    
    return soma

listaDeNumeros = [10, 2, 4, 3, 1, 9, 22, 18, 6]
print(somaPar(listaDeNumeros))