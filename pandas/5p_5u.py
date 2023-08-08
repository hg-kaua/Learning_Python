#  visualizar os 5 primeiros dados da tabela e os 5 ultimos

import pandas as pd

dsa_df = pd.read_csv("dataset.csv") 

tab_5_primeiros = dsa_df.head()
tab_5_ultimos = dsa_df.tail()

print(f"Os 5 primeiros elementos: \n")
print(tab_5_primeiros)
print(f"Os 5 ultimos elementos: \n")
print(tab_5_ultimos)
