#media_turma.py
#Peça várias notas. O usuário digita -1 para encerrar.

#No final:

#Quantidade de notas:
#Soma:
#Média:

nota = 0
quantidade = 0 
soma = 0
while nota != -1:
    print ("Digite uma nota (ou -1 para sair): ")
    nota = float(input())
    if nota != -1:
        quantidade += 1
        soma += nota

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de notas: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
