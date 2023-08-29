class Veiculo:
    
    def __init__(self, categoria):
        self.categoria = categoria
        self.marca = None
        self.ano = None
        self.preco = None
    
    def __str__(self):
        return f"""Categoria: {self.categoria}:
    - Marca: {self.marca}
    - Ano: {self.ano}
    - Preco: {self.preco}"""

carro = Veiculo("Carro")
carro.ano = 1940
carro.marca = "chevrolet"
carro.preco = 200.000

print(carro)
