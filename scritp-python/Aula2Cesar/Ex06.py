nome = str(input('Nome do Aluno: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1*2 + nota2*3 + nota3*5) / 10

if media > 7.0:
    print('{} Sua média foi {:.1f}. Aluno APROVADO!'.format(nome, media))
elif media > 5.0 and media < 6.9:
    print('{} Sua média foi {:.1f}. Aluno em RECUPERAÇÃO!'.format(nome, media))
elif media < 5.0:
    print('{} Sua média foi {:.1f}. Aluno REPROVADO!'.format(nome, media))