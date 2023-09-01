import random
class Ghost():
    
    def __init__(self):
        self.cores = ["branco", "amarelo", "roxo", "vermelho"]
    
    def color(self): 
        self.cor = random.choice(self.cores)
        return self.cor

fantasma = Ghost().color()

print(fantasma)