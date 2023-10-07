cigarros = int(input('Quantos cigarros você fuma diariamente? '))
ano = int(input('A Quanto tempo você fuma? '))

dias = ano * 365
total_cigarros = dias * cigarros

min_perdidos = total_cigarros * 10
dias = float(min_perdidos / 1440)

print("Dias de vida perdidos: {:.1f}".format(dias))