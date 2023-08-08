import pandas as pd
from convertendoEmTabela import espaco
dsa_df = pd.read_csv("dataset.csv")

print(dsa_df.head())

espaco()

print(dsa_df.isna().sum())
espaco()

# Extraindo a moda (valor que mais aparece)

moda = dsa_df["Quantidade"].value_counts().index[0]
print(moda)

# preencher na tabela com o valor da moda

espaco()
dsa_df["Quantidade"].fillna(value= moda, inplace= True)
print(dsa_df.isna().sum())