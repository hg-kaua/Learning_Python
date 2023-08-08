import random

def jogoDaForca():
    palavrasAleatorias = ["girassol", "abacaxi", "computador", "elefante", "chocolate", "bicicleta", "maravilha", "pipoca", "viagem", "felicidade"]
    palavraEscolhida = random.choice(palavrasAleatorias)
    vidas = 6
    letrasCertas = []
    
    while vidas != 0:
        letra = input("Informe uma letra: ")
        
        if letra in palavraEscolhida:
            letrasCertas.append(letra)
        else:
            vidas -= 1
        
        palavraOculta = ""
        
        for char in palavraEscolhida: # para cada letra na palavra escolhida
            if char in letrasCertas: # verifica se tem essa letra no array de letras certas
                palavraOculta += char # se tiver a palvra oculta recebe a letra
            else:
                palavraOculta += " - " # se nao recebe um tracinho
                
        print(f"Palavra: {palavraOculta}")
        print(f"Vidas: {vidas}")

        if palavraOculta == palavraEscolhida:
            print("Parabéns! Você acertou a palavra!")
            break

    if palavraOculta != palavraEscolhida:
        print(f"Fim de jogo! A palavra era '{palavraEscolhida}'.")
        

jogoDaForca()