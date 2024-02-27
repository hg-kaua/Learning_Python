import pandas as pd
import geopandas as gpd

# Caminho do arquivo Excel de entrada
excel_file = 'tmk01011.xlsx'

# Carregar o arquivo Excel em um DataFrame do pandas
df = pd.read_excel(excel_file)

for col in df.select_dtypes(include=['datetime']).columns:
    df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')

# Converter o DataFrame do pandas em um GeoDataFrame do geopandas
# Note: Isso é feito porque o geopandas tem um método to_file que suporta salvar como DBF
# Uma coluna de geometria é necessária para criar um GeoDataFrame, mesmo que não a utilizemos
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy([0]*len(df), [0]*len(df)))

# Definir o caminho do arquivo DBF de saída
dbf_file = '/Users/HK/Desktop/Teste.dbf'

# Salvar o GeoDataFrame como um arquivo DBF
gdf.to_file(dbf_file, driver='ESRI Shapefile', encoding='utf-8')

# Nota: O arquivo .dbf será criado juntamente com alguns outros arquivos auxiliares (.shp, .shx, etc.), 
# que são necessários para um shapefile completo. O arquivo .dbf pode ser utilizado independentemente.
