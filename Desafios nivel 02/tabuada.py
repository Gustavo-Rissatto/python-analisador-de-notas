# ====================================================
       # Peça um número e faça a tabuada dele de 1 até 10.
# ====================================================


numero = int(input("Digite um número para ver a tabuada: "))

while numero <= 10:
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    break