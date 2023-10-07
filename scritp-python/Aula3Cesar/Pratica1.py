total = 0

while True:
    valor = float(input("Digite o valor do produto (ou 0 para encerrar): "))

    if valor == 0:
        break
    elif valor < 0:
        print("Valor inválido")

    total += valor

    if total > 1000:
        total = total * 0.9

print(f"O valor da compra com desconto é de {total}")