def verificaPalindromo(frase):
    frase = frase.replace(" ", "").lower()
    frasePalindromo = frase[::-1]

    if(frase == frasePalindromo):
        print("É palindromo")
    else:
        print("Não é palindromo")
    

verificaPalindromo("Roma Me TEm amor")
verificaPalindromo("mano se liga ai namoral")
verificaPalindromo("A mala nada na lama")
verificaPalindromo("Fala ai mano tudo bem")
verificaPalindromo("A Rita sobre vovo verbos atira")
