from Carro import Carro
from Moto import Moto
from Fleet import Fleet


def imprimir_veiculo(veiculo):
   print(f'{veiculo} \n {veiculo.calcular_custo_manun()}\n')

ferrari = Carro("ferrari", "XYZ", 2020, 1000000, 240)
kawazaki = Moto("Kawazaki", "Ninja", 2015, 129000, 300)

gerencia = Fleet()
gerencia.add(ferrari, "Carro")
gerencia.add(kawazaki, "Moto")
print(gerencia.listar_veiculos())

