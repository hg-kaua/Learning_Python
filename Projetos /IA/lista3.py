
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

def calcular_retorno(carteira):
    return sum(acoes_empresas[i]['retorno_medio'] * carteira[i] for i in range(len(acoes_empresas)))


calcular_retorno(acoes_empresas)