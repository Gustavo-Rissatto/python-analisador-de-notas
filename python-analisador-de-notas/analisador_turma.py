print("=================================")
print("     ANALISADOR DE TURMA")
print("=================================")



nome = input("Digite o nome do aluno: ")
print("Aluno:", nome)
nota1 = float(input("Digite a nota do primeiro trimestre: "))
nota2 = float(input("Digite a nota do segundo trimestre: "))
nota3 = float(input("Digite a nota do terceiro trimestre: "))

media = (nota1+nota2+nota3)/3

print("O nome do aluno: ", nome)
print("Nota primerio trimestre: ", nota1)
print("Nota segundo trimestre: ", nota2)
print("Nota terceiro trimestre: ", nota3)
print("Média: {:.2f}".format(media))


if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")








