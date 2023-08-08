# Exercício 4: Criptografia de César
# Implemente um programa que realiza a criptografia de César. A criptografia de César é um tipo de cifra de substituição, 
# onde cada letra do texto é deslocada um número fixo de posições no alfabeto. O usuário deve fornecer o texto e o 
# deslocamento (número de posições) para a criptografia.

def Criptografia(frase, pulaCasa):
    abc = "abcdefghijklmnopqrstuvwxyz"
    criptografia = ""
    
    frase = frase.lower()
    
    for char in frase:
        if char in abc:
            index = (abc.index(char) + pulaCasa) % len(abc) #pega o index no alfadebeto e pega o modulo do tamanho para nao ultrapassar
            criptografia += abc[index]
        else:
            criptografia += char
                
    print(criptografia)
            

Criptografia("Al,oz", 3)