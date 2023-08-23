import pandas as pd

def max_common(df_a, df_b): 
    df_out = pd.concat([df_a, df_b])[df_a.columns]
    return df_out.groupby(df_out.index).max()

df_a = pd.DataFrame({
    "A": [2.5, 2.0],
    "B": [2.0, 2.0],
    "C": [2.0, 2.0]
})
df_b = pd.DataFrame({
    "C": [1.0, 8.5], 
    "B": [6.0, 1.0,],
    "D": [7.0, 9.0],
    "E": [1.0, 1.0]
})
    
print(max_common(df_a , df_b))