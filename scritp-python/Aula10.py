#condições aninhada aula 12
#if carro.esquerda:
#elif carro.direita:
#else:

nome = str(input('qual é o seu nome? '))
if nome == 'Stefferson':
    print('Que nome lindo!')
elif nome == 'Carol' or nome == 'Marcos' or nome == 'Alan':
    print('Seu nome é popular.')
elif nome in 'Ana Cláudia Jéssica Jonata':
    print('Seu nome é Legal')
else:
    print('Seu nome é comum.')
print('Tenha um bom dia, {}'.format(nome))
