consumo = int(input("Qual foi o consumo do mês: "))

if consumo <= 500:
    pagar = 0.02 * consumo + 5
elif consumo >= 500 and consumo <= 1000:
    pagar = 10 * consumo + 5
else:
    pagar = 35 * consumo + 5

print('''Você usou {}Kw de energia este mês
Sua conta de energia é de R${:.2f}'''.format(consumo, pagar))
