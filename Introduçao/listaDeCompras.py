print("Bem vindo ao mercado para iniciar suas compras so seguir os comandos abaixo:")
opc = int(input(" 1 - inserir item no carrinho\n 0 - sair do mercado: \n"))
carrinho = []
while (opc != 0):
    if (opc == 1):
        items = input("Escolha seu item: ")
        carrinho.append(items)
    opc = int(input(" 1 - inserir item no carrinho\n 0 - sair do mercado: \n"))

print(f"No seu carrinho de compras tem:")
for item in carrinho:
    print("- ", item)