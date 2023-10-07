# len(frase) para definir quantos caracteres tem a frase.
# frase[5:6:20] onde começa : até onde vai -1 : quantas casas vai pular
# frase.count('o') vai contar quantas letras tem na frase.
# frase.count('o',0,13) vai contar quantas letras tem do 0 ao 13
# frase.find('deo') vai mostrar de onde começou o "deo"
# 'palavra' in frase: existe a palavra na frase?
# frase.replace('palavra','palavra') é pra trocar a palavra.
# frase.strip() remove os espaços do inicio e do fim.
# lstrip ou rstrip para remover os espaços da direita ou da esquerda.
# frase.split() vai dividir os espaços, começando do 0 em cada palavra após os espaços
# '-'.join(frase) junta todas as palavras para juntar da frase.

frase = 'És um amor solitário, o vinho que indaga o coração, mas eu não sou o cálice que você mereça.'
print(frase.replace('coração', 'heart'))