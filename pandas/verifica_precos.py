# verificaçao de preços

import pandas as pd

'ID_Pedido', 'Data_Pedido', 'ID_Cliente', 'Segmento', 'Pais', 'Regiao',
'ID_Produto', 'Categoria', 'Nome_Produto', 'Valor_Venda', 'Quantidade'
       
df = pd.read_csv("dataset.csv")

print(df.columns)
df1 = df[df["Valor_Venda"] > 1500]
print(df1[["ID_Pedido", "Segmento", "Nome_Produto", "Valor_Venda"]])