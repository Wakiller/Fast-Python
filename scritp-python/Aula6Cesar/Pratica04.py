def media(n1, n2):
    media = (n1+n2)/2
    return media
def status(media):
    if media > 6:
        print("Aprovado!")
    elif media <= 6 and media >= 4:
        print("Recuperação!!")
    else:
        print("Reprovado!!")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

result = media(nota1, nota2)
status(result)


