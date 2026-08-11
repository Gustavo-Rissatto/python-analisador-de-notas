#Peça números até o usuário digitar 0.

#No final, mostre qual foi o maior número digitado.


maior_numero = None  # Inicializa a variável para armazenar o maior número
while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break  # Sai do loop se o usuário digitar 0
    
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero  # Atualiza o maior número se necessário

if maior_numero is not None:
    print(f"O maior número digitado foi: {maior_numero}")
else:
    print("Nenhum número válido foi digitado.")
