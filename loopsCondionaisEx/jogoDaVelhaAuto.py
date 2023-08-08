import random
import time

# consertar o codigo para fazer um relatorio de vencedores
# 1 - ler o arquivo
# 2 - fazer uma lista para cada linha
# 3 - quebrar a linha pelo espaço " "
# 4 - pegar o ultimo elemento
#     - verificar se é o O ou o X
#         - se for O countO recebe mais 1
#         - se nao countX recebe mais 1
# 5 - imprimir o contador no arquivo

# [0][0], [0][1], [0][2]
# [1][0], [1][1], [1][2]
# [2][0], [2][1], [2][2]


def atualizaTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
        
def verificaVencedor(tabuleiro):
    
    with open("loopsCondionaisEx/relatorioVencedor.txt", "a") as arquivo:   
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X" or tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] == "X":
            print("O vencedor é o X\n")
            arquivo.write("O vencedor é o X\n")
            return True
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O" or tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] == "O":
            arquivo.write("O vencedor é o O\n")
            print("O vencedor é o O\n")
            return True
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == "X" or tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == "X":
                arquivo.write("O vencedor é o X\n")
                print("O vencedor é o X\n")
                return True
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == "O" or tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == "O":
                arquivo.write("O vencedor é o O\n")
                print("O vencedor é o O\n")
                return True
       
        return False


def jogoDaVelha():

    opc = ["O", "X"]
    player1 = random.choice(opc)
    player2 = ""
    vezPlayer1 = 0
    vezPlayer2 = 0
    
    if(player1 == "X"):
        player2 = "O"
    else:
        player2 = "X"
    
    print(f"Player 1 = {player1}")
    print(f"Player 2 = {player2}")
    
    tabuleiro = []
    for i in range(3):
        linha = ["-" for i in range(3)]
        tabuleiro.append(linha)
        
    # inicializa o tabuleiro
    atualizaTabuleiro(tabuleiro)
    time.sleep(1)
    print("\n")
    posI = random.randint(0, 2)
    posJ = random.randint(0, 2)
    
    while "-" in [elemento for linha in tabuleiro for elemento in linha]:
        posI = random.randint(0, 2)
        posJ = random.randint(0, 2)

        while tabuleiro[posI][posJ] != "-":
            posI = random.randint(0, 2)
            posJ = random.randint(0, 2)

        if vezPlayer1 > vezPlayer2:
            tabuleiro[posI][posJ] = player2
            vezPlayer2 += 1
        else:
            tabuleiro[posI][posJ] = player1
            vezPlayer1 += 1

        atualizaTabuleiro(tabuleiro)
        if verificaVencedor(tabuleiro) == True:
            break
        else:
            print("\n")
            time.sleep(1.5)
    

print("-- -- -- - Bem vindo ao jogo da velha automatico - -- -- -- \n\n") 

with open("loopsCondionaisEx/relatorioVencedor.txt", "w") as arquivo:  
    pass
rodaJogo = int(input("informe quantas vezes o Jogo vai rodar: "))       

for i in range(0, rodaJogo):
    jogoDaVelha()



     