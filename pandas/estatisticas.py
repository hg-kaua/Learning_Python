import pandas as pd

df = pd.read_csv("dataset.csv")

data_frame = df.groupby(["Segmento"])["Valor_Venda"].mean()
data_frame = data_frame.reset_index()

df1 = pd.DataFrame(data_frame, columns=["Segmento", "Valor_Venda"])

df1.rename(columns={"Valor_Venda":"Media_Vendas"}, inplace=True)

print(df1)