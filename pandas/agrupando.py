# funçao para agrupor 

import pandas as pd

dsa_df = pd.read_csv("dataset.csv")

data_frame = dsa_df[["Segmento", "Regiao", "Valor_Venda"]].groupby(["Segmento", "Regiao"]).mean()

var = input('qual seu nome : ')
print(data_frame)