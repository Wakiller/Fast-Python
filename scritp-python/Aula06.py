n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
s = n1 + n2
# versão 1 do print
print(f'A soma entre {n1} e {n2} vale {s}')
# versão 2 do print
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
# versão 3 do print
print('A soma entre', n1, 'e', n2, 'vale', s)