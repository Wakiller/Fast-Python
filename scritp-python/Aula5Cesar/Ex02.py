medicoes = []
for i in range(10):
    medicao = int(input(f"Digite o valor das medições {i+1}: ")) #adicionar as medições na lista
    medicoes.append(medicao)

arquivo = open("Exemplo.txt", "w") #abri o arquivo
for medicao in medicoes: #colocamos as medições no arquivo em cada linha
    arquivo.write(str(medicao)+'\n')
arquivo.close()

contagem = 0

arquivo = open("Exemplo.txt", "r")
linhas = arquivo.readline()
arquivo.close()

for i in range(1, 10+1):
    medicao_atual = int(linhas[i])
    medicao_anterior = int(linhas[i-1])

    if medicao_atual > medicao_anterior:
        contagem+=1

    print('{}'.format(contagem))