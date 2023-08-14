import pandas as pd

df = pd.DataFrame({
        "Produto": ["Geladeira", "Micro-Ondas", "Ventilador", "Misturadeira", "Liquidificador"],
        "Preco_Compra": [1200.50, 400.00,150.00,300.00,80.00],
        "Preco_Venda": [1800.00, 600.00, 180.00, 400.00, 100.00],
        "Quantidade_Vendida": [30, 50, 120, 25, 80]
        }, 
        index=["1","2","3","4","5"]
    )

data_frame = df.groupby("Produto")[["Preco_Compra", "Preco_Venda"]].sum()

print(df)
print(data_frame)