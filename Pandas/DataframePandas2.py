import pandas as pd

aluno = [['Stefferson', '6,5'],
         ['Carolina', '9.5'],
         ['Vladimir', '7.5'],
         ['Auriele', '4.5'],
         ['Alisson', '7.0']]

df = pd.DataFrame(aluno, columns=['Nome', 'Média'])
status = ['Reprovado', 'Aprovado', 'Aprovado', 'Reprovado', 'Aprovado']
df['Status'] = status
#print(df)
#selecionando apenas aprovados
df_status = df_aluno[df_aluno['Status'] == "Aprovado"]
print(df_status)