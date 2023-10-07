nota = 0
soma = 0
contar = 0

while True:
    nota = float(input("Digite a nota do aluno: "))

    if nota == -1:
        break

    soma+=nota
    contar+=1

media = soma/contar
print('A média das notas foi {:.2f}'.format(media))
