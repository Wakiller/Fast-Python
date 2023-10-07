vel = int(input("Qual a velocidade do carro: "))

multa = (vel - 80) * 5.00

if vel > 80:
    print('Você foi multado por excesso de velocidade, o valor da multa foi de R${:.2f}'.format(multa))