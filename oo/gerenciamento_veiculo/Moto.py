from Veiculo import Veiculo

class Moto(Veiculo):
    
    def __init__(self, marca, modelo, ano, preco, vel_maxima= 100):
        super().__init__(marca, modelo, ano, preco)
        self.vel_maxima = vel_maxima
    
    def calcular_custo_manun(self):
        return super().calcular_custo_manun()
    
    def __str__(self):
        return super().__str__() + f"\n    - Velocidade Máxima: {self.vel_maxima}"