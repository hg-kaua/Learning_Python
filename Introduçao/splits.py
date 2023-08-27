def solution(s):
    lista = []
    nova_letra = ""
    for letra in s:
        if len(nova_letra) < 2:
            nova_letra += letra
        elif len(nova_letra) ==  2:
            lista.append(nova_letra)
        else:
            nova_letra = ""
    return lista

print(solution("abcd"))