# operadores aritimeticos
# + = adição
# - = subtração
# * = multiplicação
# / = divisão
# // = duvisão de numeros inteiros
# ** = potencia
# % = resto da divisão
# == dois igual é igual a quanto?

#ordem de precedência
#1 resolve primeiro ()
#2 resolve as **
#3 resolve * /  //  %
#4 + e -

nome = input('Qual o seu nome? ')
print('Prazer em conhece-lo {}'.format(nome))

n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A some é {}, o produte é {} e a divisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira é {} e a potência é {}'.format(di, e))
