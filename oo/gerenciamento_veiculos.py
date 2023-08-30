class Veiculo:
    
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def calcular_custo_manun(self):
        custo_carro = 100 + (2023 - self.ano) * 30
        return f"Custo manutenção: R${custo_carro}"
    
    def __str__(self):
        return f"""
    - Marca: {self.marca}
    - Modelo: {self.modelo}
    - Ano: {self.ano}
    - Preco: {self.preco}"""

class Carro(Veiculo):
    
    def __init__(self, marca, modelo, ano, preco, categoria = "Carro", vel_maxima = 150):
        super().__init__(marca, modelo, ano, preco)
        self.categoria = categoria
        self.vel_maxima = vel_maxima
    
    def calcular_custo_manun(self):
        return super().calcular_custo_manun()
    
    def __str__(self):
        return f"Categoria: {self.categoria}" + super().__str__() + f"\n    - Velocidade Máxima: {self.vel_maxima}"


class Moto(Veiculo):
    
    def __init__(self, marca, modelo, ano, preco):
        pass
    
ferrari = Carro("ferrari", "XYZ", 2020, 1000000, vel_maxima=240)


print(ferrari.calcular_custo_manun())