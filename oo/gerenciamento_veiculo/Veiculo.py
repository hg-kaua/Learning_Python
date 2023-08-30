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


    