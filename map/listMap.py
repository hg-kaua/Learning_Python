# map() é uma funçao que aplica uma determinada funçao a cada elemnento de uma estrutura de dados

def potencia(x):
    return x**2

numeros = [1,2,3,4,5,6,7,8]
numerosAoQuadrado = (list(map(potencia, numeros)))
print(numerosAoQuadrado)

for numero in list(map(potencia, numeros)):
    print(f"{numero} ")