class Data:
    # construtor padrao da classe / self: toda funçao dentro da classe começa com self
    # dia mes e ano sao parametros do construtor
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia 
        self.mes =  mes
        self.ano = ano 
    
    # palavra reservada que retorna uma string
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
    
data_nasc = Data(23, 10, 2002) # chamando a classe e criando objeto de instancia
data_padrao = Data()

print(f"Data padrão da classe {data_padrao}")
print(f"Ola meu nome é hugo e eu nasci no dia {data_nasc}")