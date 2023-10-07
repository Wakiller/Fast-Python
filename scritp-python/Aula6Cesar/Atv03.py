from datetime import date
def auxilio(ano):
    ano_atual = date.today().year
    idade = ano_atual-ano
    if idade >= 4 and idade <= 16:
        print("Auxilio autorizado.")
    else:
        print("Auxilio negado.")
ano = int(input("Digite o seu ano de nascimento: "))
auxilio(ano)