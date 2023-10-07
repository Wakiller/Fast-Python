n = int(input('Digite o número: '))
soma_divisor = 0
for i in range(1, n):
    if n%i==0:
        soma_divisor+=i

if n == soma_divisor:
    print('Número Perfeito.')
else:
    print('Não é um número perfeito.')