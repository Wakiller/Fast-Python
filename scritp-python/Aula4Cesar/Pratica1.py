notas = []
#
for i in range(5):
    nota = float(input(f'Digite a nota: {i+1}: '))
    notas.append(nota)
#soma e a media das notas
media = sum(notas) / 5
print('A média da turma é {:.2f}'.format(media))
print('Notas superiores à média:')
for nota in notas:
    if nota > media:
        print(nota)
