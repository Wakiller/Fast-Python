pergunta = []

print('Responda com "sim" ou "não" as perguntas.')
pergunta.append(str(input('Conhece a vítima do furto? ')))
pergunta.append(str(input('Esteve no local do furto? ')))
pergunta.append(str(input('Mora perto da Vitima? ')))
pergunta.append(str(input('A vítima lhe devia? ')))
pergunta.append(str(input('Já trabalhou com a vítima? ')))

soma = 0
for p in pergunta:
    if p == "SIM":
        soma += 1
if soma == 2:
    print("Suspeita")
elif soma == 3 or soma == 4:
    print("Cúmplice")
elif soma == 5:
    print("Ladrão")
else:
    print("Inocente")