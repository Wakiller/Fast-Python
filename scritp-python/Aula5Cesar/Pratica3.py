arquivo = open('Exemplo.txt', 'w')

disciplina = input("Em que disciplina você está: ")
turma = input('Qual a sua turma: ')

arquivo.write(disciplina + '\n')
arquivo.write(turma)

arquivo.close()

print(arquivo)