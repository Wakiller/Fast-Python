from datetime import date
n = date.today().year
maioridade = 0
menoridade = 0
for i in range(5):
    ano = int(input('Ano de Nascimento: '))

    if n - ano >= 18:
        maioridade+=1
    else:
        menoridade+=1

print('{} são menores de idade e {} são maior de idade.'.format(menoridade, maioridade))