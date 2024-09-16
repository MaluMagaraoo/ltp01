# Lista de notas dos alunos

notas = [6.3, 7.5, 9.2, 5.1, 6.8]

media = sum(notas) / len(notas)

notas_acima_de_seis = len([nota for nota in notas if nota > 6])

print(f"Média das notas: {media:.2f}")
print(f"Quantidade de notas acima de 6: {notas_acima_de_seis}")