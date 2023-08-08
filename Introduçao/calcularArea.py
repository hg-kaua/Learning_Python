print('Bem vindo ao programa que calcula áreas!!')

objetoParaCalcular = int(input(' 1 - Quadrado \n 2 - Retângulo \n 3 - triângulo\n Informe aqui: '))

if (objetoParaCalcular == 1 ):
    base = int(input("Informe o base do quadrado: "))
    area = base*base
    print(f'A área do quadrado é {area}m2')
elif (objetoParaCalcular == 2):
    altura = int(input("Informe a altura do retângulo: "))
    base = int(input("Informe a base do retângulo: "))
    area = base*altura
    print(f'A área do retânqulo é {area}m2')
elif (objetoParaCalcular == 3):
    altura = int(input("Informe a altura do triângulo: "))
    base = int(input("Informe a base do triângulo: "))
    area = (base * altura)/2
    print(f"A área do triângulo é {area}m2")
else: 
    print("Informe um valor valido na prox vez")