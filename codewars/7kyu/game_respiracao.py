# Criar funçao que diz se o personagem sobreviveu ao mergulho ou nao : True ou False
# medidor de respiraçao = 10 
# diminui 2 em baixo d'agua e reabastece 10 acima da agua

def diving_minigame(lst):
    medidor = 10
    
    for altitude in lst:
        if altitude >= 0:
            if medidor < 10:
                medidor += 4
            if medidor >= 10:
                medidor = 10
        else:
            if medidor > 0:
                medidor -= 2
            if medidor <= 0:
                break
        print(medidor, " ")
    
    return True if medidor > 0 else False
    pass


print(diving_minigame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(diving_minigame([-5, -5, -5, -5, -5, 2, 2, 2, 2, 2, 2, 2, 2]))
print(diving_minigame([-15, 11, -1, -11, -9, -6, -11, 8, -3, 19, 2, -2, -17, -17, 3, 8, -3, -11]))