d = 0
npar = 0
nimpar = 0
for i in range(10):
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        npar+=1
    else:
        nimpar+=1

print('{} números são Pares.'.format(npar))
print('{} números são Impares.'.format(nimpar))
