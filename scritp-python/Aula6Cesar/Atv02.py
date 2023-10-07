def imprimir(numero):
    for i in range(1, numero+1):
        print(i, end=" ")
while True:
    numero = int(input("Digite um valor inteiro: "))

    if numero==0:
        break

    imprimir(numero)