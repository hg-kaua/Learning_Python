import random

# Definir informações sobre as ações das empresas
acoes_empresas = [
    {"codigo": "BBAS3", "retorno_medio": 0.37, "desvio_padrao": 2.48},
    {"codigo": "BBDC4", "retorno_medio": 0.24, "desvio_padrao": 2.16},
    {"codigo": "ELET6", "retorno_medio": 0.14, "desvio_padrao": 1.95},
    {"codigo": "GGBR4", "retorno_medio": 0.30, "desvio_padrao": 2.93},
    {"codigo": "ITSA4", "retorno_medio": 0.24, "desvio_padrao": 2.40},
    {"codigo": "PETR4", "retorno_medio": 0.19, "desvio_padrao": 2.00},
    {"codigo": "CSNA3", "retorno_medio": 0.28, "desvio_padrao": 2.63},
    {"codigo": "TNLP4", "retorno_medio": 0.18, "desvio_padrao": 2.14},
    {"codigo": "USIM5", "retorno_medio": 0.25, "desvio_padrao": 2.73},
    {"codigo": "VALE5", "retorno_medio": 0.24, "desvio_padrao": 2.47},
    {"codigo": "MGLU3", "retorno_medio": 0.31, "desvio_padrao": 2.7},
    {"codigo": "HAPV3", "retorno_medio": 0.26, "desvio_padrao": 2.13},
    {"codigo": "BRAV2", "retorno_medio": 0.33, "desvio_padrao": 2.00},
    {"codigo": "ESPA3", "retorno_medio": 0.23, "desvio_padrao": 2.20},
    {"codigo": "POWE3", "retorno_medio": 0.29, "desvio_padrao": 1.99},
    {"codigo": "HBRE3", "retorno_medio": 0.32, "desvio_padrao": 2.83},
    {"codigo": "CMIN3", "retorno_medio": 0.22, "desvio_padrao": 2.65},
    {"codigo": "INTB3", "retorno_medio": 0.30, "desvio_padrao": 2.80},
    {"codigo": "CASH3", "retorno_medio": 0.23, "desvio_padrao": 2.32},
    {"codigo": "MOSI3", "retorno_medio": 0.25, "desvio_padrao": 2.16},
    {"codigo": "SEQL3", "retorno_medio": 0.25, "desvio_padrao": 2.65},
    {"codigo": "VAMO3", "retorno_medio": 0.25, "desvio_padrao": 2.50},
    {"codigo": "WEST3", "retorno_medio": 0.27, "desvio_padrao": 2.53},
]

# Função para calcular o valor de retorno para um portfólio de ações
def calcular_retorno(portfolio):
    retorno_total = sum(acoes_empresas[i]["retorno_medio"] * portfolio[i] for i in range(len(acoes_empresas)))
    return retorno_total

# Função para calcular o risco para um portfólio de ações
def calcular_risco(portfolio):
    risco_total = (sum(acoes_empresas[i]["desvio_padrao"] ** 2 * portfolio[i] for i in range(len(acoes_empresas)))) ** 0.5
    return risco_total

# Função de aptidão (fitness) para o AG
def fitness(portfolio, objetivo_retorno):
    retorno = calcular_retorno(portfolio)
    risco = calcular_risco(portfolio)
    
    penalidade = 0
    if retorno < objetivo_retorno:
        penalidade = objetivo_retorno - retorno
    
    return retorno - penalidade

# Função para criar um indivíduo (portfólio) aleatório
def criar_individuo():
    return [random.randint(0, 1) for _ in range(len(acoes_empresas))]

# Função para mutar um indivíduo
def mutar_individuo(individuo):
    index = random.randint(0, len(individuo) - 1)
    individuo[index] = 1 - individuo[index]

# Algoritmo Genético
def algoritmo_genetico(objetivo_retorno, populacao_size=100, geracoes=100, taxa_mutacao=0.1):
    populacao = [criar_individuo() for _ in range(populacao_size)]
    
    for geracao in range(geracoes):
        populacao = sorted(populacao, key=lambda x: -fitness(x, objetivo_retorno))
        elite = populacao[:10]  # Mantenha os 10 melhores indivíduos
        
        for i in range(len(populacao) - 10):
            pai = random.choice(elite)
            mae = random.choice(elite)
            filho = pai[:len(pai) // 2] + mae[len(mae) // 2:]
            if random.random() < taxa_mutacao:
                mutar_individuo(filho)
            elite.append(filho)
        
        populacao = elite
    
    melhor_portfolio = max(populacao, key=lambda x: fitness(x, objetivo_retorno))
    return melhor_portfolio

# Encontre o melhor portfólio para cada objetivo de retorno
objetivos_retorno = [0.10, 0.20, 0.25, 0.30]
for objetivo in objetivos_retorno:
    melhor_portfolio = algoritmo_genetico(objetivo)
    print(f"Melhor portfólio para objetivo de retorno {objetivo * 100}%:")
    for i, acao in enumerate(acoes_empresas):
        if melhor_portfolio[i] == 1:
            print(f"({acao['codigo']})")
    print()

