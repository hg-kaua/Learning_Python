class Veiculo:
    
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def calcular_custo_manun(self):
        return 100 + (2023 - self.ano) * 30
    
    def __str__(self):
        return f"""
    - Marca: {self.marca}:
    - Modelo: {self.modelo}
    - Ano: {self.ano}
    - Preco: {self.preco}"""

class Carro:
    def __init__(self, marca, modelo, ano, preco, categoria = "Carro", vel_maxima = 150):
        super().__init__(marca, modelo, ano, preco)
        self.categoria = categoria
        self.vel_maxima = vel_maxima
    
    def calcular_custo_manun(self):
        super().calcular_custo_manun()
    
    def __str__(self):
        super().__str__()

ferrari = Carro("ferrari", "ferrari", 2020, 1000000, vel_maxima=240)
print(ferrari)