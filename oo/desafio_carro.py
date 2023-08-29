class Carro:
    def __init__(self, vel_maxima= 150):
        self.vel_maxima = vel_maxima
        self.vel_atual = 0
    
    def acelerar(self, delta= 5):
        self.vel_atual = delta
        
        if self.vel_atual < self.vel_maxima and self.vel_atual <= self.vel_maxima - delta:
            self.vel_atual += delta
        else:
            self.vel_atual = self.vel_maxima
        return(f"Acelerando.. {self.vel_atual}Km")
    
    def frear(self, delta= 20):
        self.vel_atual = delta
        
        if self.vel_atual > 0 and self.vel_atual >= delta:
            self.vel_atual += delta
        else:
            self.vel_atual = 0
        return(f"freando.. {self.vel_atual}Km")

if __name__ == '__main__':
    c1 = Carro(180)
    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(20))