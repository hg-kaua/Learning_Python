def verificaPrimo(num):
    if(num <= 1):
       return False
    elif (num == 2):
        return True
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            else:
                return True


num = int(input("Informe o valor a ser verificado: "))
if verificaPrimo(num) == True:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")