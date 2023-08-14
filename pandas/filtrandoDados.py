import pandas as pd

dsa_df = pd.read_csv("Learning_Python/dataset.csv")
# isin() verifica se os parametros passados entre colchetes existem dentro do arquivo
# shape retorna o numero exato de linhas e colunas
data_frame = dsa_df[dsa_df["Quantidade"].isin([8,10])].shape
data_frame2 = dsa_df[dsa_df["Quantidade"].isin([8,10])]

# Imprime as linhas e colunas
print(data_frame)
# Imprime as 10 primeiras linhas
# print(data_frame2.head(20))

# Utilizando operadores logicos

data_frame3 = dsa_df[ (dsa_df["Segmento"] == "Home Office") & (dsa_df["Regiao"] == "South") ]

data_frame4 = dsa_df[ (dsa_df["Quantidade"] > 15) | (dsa_df["Regiao"] != "South") & (dsa_df["Regiao"] != "West") ]

print(data_frame3.head(3))
print("\n")
print(data_frame4.tail(13))
