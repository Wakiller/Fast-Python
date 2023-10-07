import pandas as pd

dados = {
    'Nome': ['Stefferson', 'Marcos', 'Carol'],
    'Cidade': ['Manaus', 'Campinas', 'Governador Valadares'],
    'Idade': [26,27,26],
    'Telefone': ['(92)981593007', '(81)985674123', '(93)958421563']
}
df = pd.DataFrame(dados)
print(df)