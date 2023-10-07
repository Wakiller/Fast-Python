def mult_num(num1, num2): #funções
    return num1*num2

def soma_num(num1, num2):
    return num1+num2

def sub_num(num1, num2):
    return num1-num2

def div_num(num1, num2):
    if num1 >= num2:
        return num1/num2
    else:
        return num2/num1

#Programa Principal
resp = input("Deseja fazer uma operação? [S] Sim ou [N] Não: ")
while resp=="S":
    op = input("Escolha a operação [+]Soma\n [-]Subtração\n [*]Multiplicar \n [/]Divisão)\n: ")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if op == '+':
        print(soma_num(n1, n2))
    elif op == '-':
        print(sub_num(n1, n1))
    elif op == '*':
        print(mult_num(n1, n2))
    else:
        print(div_num(n1, n2))

    continuar = input("Deseja fazer outra operação? [S]Sim ou [N]Não")