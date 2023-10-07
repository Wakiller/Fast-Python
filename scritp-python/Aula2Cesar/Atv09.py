reajuste = int(input('Quanto tempo sem reajuste? '))
tempo = int(input('Quanto tempo de cargo o funcionário tem? '))
nome = str(input('Nome do funcionário: '))
salario = float(input('Salario atual do funcionário: '))

if reajuste > 2:
    if tempo > 10:
        aumento = salario * 0.30 + salario
    elif tempo >= 5 and tempo <=10:
        aumento = salario * 0.20 + salario
    else:
        aumento = salario * 0.10 + salario
    print('''
    Funcionário {}
    Tempo de cargo {} anos
    Salário atual R${:.2f}
    Novo Salário R${:.2f}'''.format(nome, tempo, salario, aumento))
else:
    print('Não está apto ao reajuste.')

