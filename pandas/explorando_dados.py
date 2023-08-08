import pandas as pd

dates = pd.date_range("2023-01-01", periods=4, freq="W")

data_frame = pd.DataFrame({
    "Produto": ["Geladeira", "Micro-Ondas", "Ventilador", "Misteira"],
    "Preço_compra": [3400.30,1230.00,682.79, 430.10]
     })

data_frame["Data_Compra"]  = dates

index_alterado = range(1, len(data_frame) + 1)
data_frame.index = index_alterado

print(data_frame)
