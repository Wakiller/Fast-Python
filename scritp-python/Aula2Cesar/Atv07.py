idade = int(input("Qual a sua idade? "))

if idade < 4 or idade > 60:
    print("Entrada gratuíta.")
elif idade >= 4 and idade <= 18:
    print("Entrada custa R$20.00")
else:
    print('Entrada custa R$30.00')