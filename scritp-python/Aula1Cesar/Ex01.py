largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = largura * altura
tinta = area / 2

print("A área da parede é {:.1f}m² e são necessárias {:.1f}l de tintas para pintar a parede.".format(area, tinta))