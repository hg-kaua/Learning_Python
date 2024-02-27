
import random

# Definição do problema da mochila (itens, capacidade da mochila)
itens = [(1, 10, 5), (2, 5, 4), (3, 15, 8), (4, 7, 3), (5, 6, 2)]  # Formato: (ID, Valor, Peso)
capacidade_mochila = 10

# Parâmetros do algoritmo genético
tamanho_populacao = 50
taxa_mutacao = 0.1
num_geracoes = 100

# Função de fitness: Retorna o valor total dos itens na mochila
def calcular_fitness(individuo):
    valor_total = 0
    peso_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            valor_total += itens[i][1]
            peso_total += itens[i][2]
    if peso_total > capacidade_mochila:
        return 0  # Penaliza soluções inválidas (peso total excede a capacidade)
    else:
        return valor_total

# Inicialização da população
populacao = []
for _ in range(tamanho_populacao):
    individuo = [random.randint(0, 1) for _ in range(len(itens))]  # Representação binária dos itens
    populacao.append(individuo)

# Algoritmo Genético
for geracao in range(num_geracoes):
    # Avaliação da população
    fitness_populacao = [calcular_fitness(individuo) for individuo in populacao]

    # Seleção (Torneio)
    nova_populacao = []
    for _ in range(tamanho_populacao):
        torneio = random.sample(range(tamanho_populacao), 5)  # Seleciona aleatoriamente 5 indivíduos para o torneio
        vencedor = torneio[0]
        for i in torneio:
            if fitness_populacao[i] > fitness_populacao[vencedor]:
                vencedor = i
        nova_populacao.append(populacao[vencedor])

    # Crossover (Ponto de corte único)
    for i in range(0, tamanho_populacao, 2):
        ponto_corte = random.randint(1, len(itens) - 1)
        pai1 = nova_populacao[i]
        pai2 = nova_populacao[i + 1]
        filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
        filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
        nova_populacao[i] = filho1
        nova_populacao[i + 1] = filho2

    # Mutação
    for i in range(tamanho_populacao):
        if random.random() < taxa_mutacao:
            gene_mutante = random.randint(0, len(itens) - 1)
            nova_populacao[i][gene_mutante] = 1 - nova_populacao[i][gene_mutante]  # Inverte o bit

    # Substituição da população
    populacao = nova_populacao

# Encontrar a melhor solução após as gerações
melhor_individuo = populacao[fitness_populacao.index(max(fitness_populacao))]

# Mostrar a melhor solução
print("Melhor solução encontrada:")
for i in range(len(itens)):
    if melhor_individuo[i] == 1:
        print(f"Item {itens[i][0]} (Valor: {itens[i][1]}, Peso: {itens[i][2]})")

print(f"Valor Total: {calcular_fitness(melhor_individuo)}")
