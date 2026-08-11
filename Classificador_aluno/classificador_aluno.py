#O programa recebe:
#Nome:
#Nota 1:
#Nota 2:
#Nota 3:
#Calcula a média e classifica:
#Média >= 9      → Excelente
#Média >= 7      → Aprovado
#Média >= 5      → Recuperação
#Média < 5       → Reprovado
#Saída:
#============================
#RESULTADO DO ALUNO
#============================
#Aluno: Gustavo
#Média: 8.33
#Situação: Aprovado


nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    situacao = "Excelente"
elif media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print ("============================")
print ("RESULTADO DO ALUNO")
print ("============================")
print ("Aluno:", nome)
print ("Média:", f"{media:.2f}")
print ("Situação:", situacao)
print ("============================")