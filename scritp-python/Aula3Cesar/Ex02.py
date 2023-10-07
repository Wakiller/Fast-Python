sexo_fem_idade = 0
olhos_cabelo = 0

for i in range(5):
    print('''Qual o seu Sexo?
    [ 1 ] Masculino
    [ 2 ] Feminino''')
    lista = [1, 2]
    sexo = int(input('Digite uma opção: '))
    print('''Qual a cor do seu cabelo?
    [ 1 ] Preto
    [ 2 ] Castanho
    [ 3 ] Loiro''')
    lista = [1, 2, 3]
    cab = int(input('Digite uma opção: '))
    print('''Qual a cor dos seus olhos?
    [ 1 ] Azuis
    [ 2 ] Verdes
    [ 3 ] Castanhos''')
    olho = int(input('Digite uma opção: '))
    id = int(input('Digite a sua Idade: '))

    if sexo == 2 and idade >=18 and idade <=35:
        sexo_fem_idade+=1
    else:
        olhos_cabelo+=1

print('{} pessoas são Mulheres com idade entre 18-35 anos.'.format(sexo_fem_idade))
print('{} pessoas tem os olhos castanhos e cabelo preto'.format(olhos_cabelo))
