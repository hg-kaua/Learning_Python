
num1 = int(input("informe o primeiro valor: "))
num2 = int(input("informe o segundo valor: "))
operaçao = input(" 1 - Soma(+)\n 2 - Subtração(-)\n 3 - Multiplicação(x)\n 4 - Divisão(/): ")


if (operaçao == "+"):
    print(f"Resultado: {num1 + num2}")
elif (operaçao == "-"):
    print(f"Resultado: {num1 - num2}")
elif (operaçao == "x"):
    print(f"Resultado: {num1 * num2}")
elif (operaçao == "+"):
    print(f"Resultado: {num1 / num2}")