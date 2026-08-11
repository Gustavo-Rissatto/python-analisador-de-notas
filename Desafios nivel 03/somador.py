#somador.py
#eça números até o usuário digitar 0.

#No final mostre:

#Quantidade de números: X
#Soma dos números: Y 

numero = 1
quantidade = 0
soma = 0
while numero != 0:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero != 0:
        quantidade += 1
        soma += numero
    else:
        print ("Quantidade de tentativas: ", quantidade, "Soma dos números: ", soma)
