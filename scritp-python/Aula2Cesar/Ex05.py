op = str(input('Digite seu Estado Civil'))

if op == "S":
    print("Pessoa solteira.")
elif op == "C":
    print('Pessoa Casada.')
elif op == "V":
    print('Pessoa Viúva.')
else:
    print('Opção Inválida.')