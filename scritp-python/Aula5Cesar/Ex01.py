frase = input("Por favor, insira a frase: ")

palavra_antiga = input("Por favor, insira uma palavra que está contida na frase: ")

palavra_nova = input(
    "Por favor, insira outra palavra que você deseja substituir no lugar da primeira palavra inserida: ")

if palavra_antiga in frase:

    indice_inicio = frase.find(palavra_antiga)
    indice_fim = indice_inicio + len(palavra_antiga)

    frase_modificada = frase[:indice_inicio] + palavra_nova + frase[indice_fim:]

    print(frase_modificada.upper())
else:
    print("A palavra inserida não está contida na frase.")