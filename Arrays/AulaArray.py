import numpy as np

notas = [1, 2, 3, 4, 5]
nota = []

for i in range(5):
    num = float(input("Digite a nota: "))
    nota.append(num)

listNumpy = np.array(notas)
media = listNumpy.mean()
print("A média do aluno é {}".format(media))