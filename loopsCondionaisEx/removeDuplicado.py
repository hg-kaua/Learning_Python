def removeDuplicadas(lista):
    return set(lista) #remove os elementos repetidos

lista = [1,1,1,1,1,1,1,1,3]

print(f"O tamanho da lista: {len(lista)} elementos")
print(removeDuplicadas(lista))