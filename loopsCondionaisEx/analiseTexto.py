# Crie uma função que receba um texto como entrada e realize as seguintes análises:

# Conte o número total de palavras no texto.
# Conte quantas vezes cada palavra aparece no texto e exiba as palavras mais frequentes.
# Calcule a média de comprimento das palavras no texto.

def get_texto(text):
    contador_letras(text)
    palavra_frequente(text)

def contador_letras(text):
    count = 0
    for char in texto:
        if char.isalpha():
            count += 1
    return count

def palavra_frequente(text):
    word_text = text.lower()
    word_list = word_text.split(" ")
    maior_freq = 0
    
    # vou fazer um list comprehesion (ainda vou estudar melhor)
    word_freq = [word_list.count(w) for w in word_list]
    
    for freq in word_freq:
        if freq > maior_freq:
            maior_freq = freq
    
    print(f"Frequencia: {list(zip(word_list,word_freq))}")
    print(f"Maior frequencia: {maior_freq}")
    

# TERMINAR
def media_comprimento(text):
    word_text = text.lower()
    
    for char in word_text: 
        taman
    