import pandas as pd

df = pd.read_csv("Learning_Python/dataset.csv")

# dsa_df = df.loc["ID_Pedido"]

print(df.loc[[1, 3]])