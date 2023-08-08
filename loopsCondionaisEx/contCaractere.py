# outra maneira
# from collections import Counter

# def dictCaracter(frase):
#     frase = frase.replace(" ", "")
#     return dict(Counter(frase))

# print(dictCaracter("ola!! como vai voce? esta andando muito ocupado, haha"))

def dictCaracter(frase):
    frase = frase.replace(" ", "")
    dicionario = {}
    for char in frase:
        dicionario[char] = frase.count(char)
    return dicionario
    

print(dictCaracter("ola!! como vai voce? esta andando muito ocupado, haha"))
