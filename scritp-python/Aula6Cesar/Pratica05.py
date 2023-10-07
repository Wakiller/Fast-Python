from random import randint
def sorteio():
    numero = []
    for i in range(5):
        numero.append(randint(0,99))
    return numero

def somapar(numero):
    pares = []
    for i in range(5):
        if numero%2==0:
            pares.append(i)
        print("A soma dos números pares é {}".format(pares))
somapar(sorteio())
