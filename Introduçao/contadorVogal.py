def verificaVogal(frase):
    vogais = "a e i o u"
    vogais = vogais.split(" ")
    contVogal = contConsoante = 0
    
    frase = frase.lower()
    
    for i in range(len(frase)):
        if (frase[i].isalpha()):
            if(frase[i] in vogais):
                contVogal += 1
            else:
                contConsoante += 1
    print(f"Número de vogais: {contVogal} \nNúmero de consoantes: {contConsoante}")
    
verificaVogal("o29@1latu 32  4321  234 dobem")
    
