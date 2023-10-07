def media_num(num1, num2):
    media = (num1+num2)/2
    return  media

altura1 = float(input("Digite a altura 1: "))
altura2 = float(input("Digite a altura 2: "))

media = media_num(altura1, altura2)

print("A média das alturas é {:.2f}".format(media))