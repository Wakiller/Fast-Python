n = int(input('Quantos minutos faltam? '))
tempo1 = int(input('Tempo do presente 1: '))
tempo2 = int(input('Tempo do presente 2: '))
tempo = tempo2 + tempo1

if tempo <= n:
    print('Farei hoje.')
else:
    print('Deixo para amanhã.')