# ====================================================================================
        # Peça uma senha continuamente. Só encerre quando o usuário digitar: python123
# ====================================================================================


senha = int(input("Digite a senha: "))
while senha != "python123":
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")
else:
    senha == "python123"
    print("Senha correta. Acesso permitido.")