import pandas as pd

df_vacinados = pd.read_csv('vacinados.csv',sep=';')
df_vacinados = df_vacinados[(df_vacinados['idade'] > 60) & (df_vacinados['sexo'] =='FEMININO')]
print(df_vacinados[['idade','sexo']])