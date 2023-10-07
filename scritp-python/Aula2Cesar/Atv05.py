nome = str(input('Qual o seu nome? '))
sexo = str(input('Qual o seu sexo? M para masculino e F para feminino'))
compra = float(input("Qual o valor da sua compra? "))

pagar = compra -

if lista == "F":
    valor = compra * 0.15
else:
    valor = compra * 0.05
pagar = compra - valor

print('''Olá {}
você está recebdo um desconto de {}%
sua compra ficou de R${:.2f}''')