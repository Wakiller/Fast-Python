import os
os.system("cls")
arquivo = open('FASTPRG.txt', 'r', encoding="utf8") #Abrir o Arquivo.
dados = arquivo.read() #manipulação em quantidade de caractere.
palavras = dados.split() #manipulação em quantidade de palavras, transformando em uma lista.

arquivo.close()

print(dados)
print('Quantidade de caractere:', len(dados))
print('quantidade de palavras:', len(palavras))
