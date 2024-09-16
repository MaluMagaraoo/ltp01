turma = ('André', 'Fernanda', 'Luiz')

nome_aluno = input("Digite o nome de um aluno: ")

if nome_aluno in turma:
    print(f"{nome_aluno} está na turma.")
else:
    print(f"{nome_aluno} não está na turma.")