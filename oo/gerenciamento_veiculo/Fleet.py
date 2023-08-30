from Veiculo import Veiculo

# classe de gerenciamento
class Fleet:
    
    def __init__(self):
        self.lista_veiculo = {}
        
    def add(self, veiculo, categoria):
        self.categoria = categoria
        self.lista_veiculo[categoria] = veiculo  
        return self.lista_veiculo
    
    def procurar_veiculo(self, marca_veiculo):
        self.marca_veiculo = marca_veiculo
        return [veiculo for veiculo in self.lista_veiculo if veiculo.marca == marca_veiculo]

    def listar_veiculos(self):
        info_veiculos = ""
        for categoria, veiculo in self.lista_veiculo.items():
            info_veiculos += f"\n- Categoria: {categoria}\t {veiculo}\n"
        return info_veiculos