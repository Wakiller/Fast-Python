banho = 0
tosa = 0
banho_tosa = 0
outros = 0

for i in range(5):
    print('''Escolha um serviço
    [ 1 ] Banho
    [ 2 ] Tosa
    [ 3 ] Banho & Tosa
    [ 4 ] Outros''')
    op = int(input(''))

    if op == 1:
        banho+=1
    elif op == 2:
        tosa+=1
    elif op == 3:
        banho_tosa+=1
    elif op == 4:
        outros+=2

print('''Os pedidos de hoje são
{} Banho
{} Tosa
{} Banho e Tosa
{} Outros'''.format(banho, tosa, banho_tosa, outros))
