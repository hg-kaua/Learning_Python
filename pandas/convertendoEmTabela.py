from pandas import DataFrame 
import numpy as np

def espaco():
    print(f"\n+++++++++++++++++++++++++++++++++++++++++\n")
    
    
dados = {"Estado": ["Rio de janeiro", "São Paulo", "Minas Gerais", "Santa Catarina", "Parana", "Brasilia"],
         "Ano": [2002, 1978, 1979, 2001, 2007, 2016],
         "Taxa Desemprego": [1.5, 1.7, 2.0, 2.4, 1.2, 1.9],}

# da biblioteca pandas importa a funçao DataFrame

# converte o dicionario em um dataframe
df = DataFrame(dados)

# df.head() mostra so os 5 primeiros
print(df)
espaco()

# reoganizar colunas 
tab = DataFrame(dados, columns = ["Estado", "Taxa Desemprego", "Ano"])
print(tab)

# criando um novo campo

df2 = DataFrame(dados,
                columns=["Estado", "Taxa Desemprego", "Taxa Crescimento", "Ano"],
                index=["estado 1", "estado 2", "estado 3", "estado 4", "estado 5", "estado 6"])

espaco()
print(df2)
espaco()

# print(df2.describe()) faz uma analise estatisca de valores numericos

df2["Taxa Crescimento"] = np.arange(6.) 
print(df2)
