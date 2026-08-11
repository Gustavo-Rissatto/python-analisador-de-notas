def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


nome = input("Digite o nome do aluno: ")
nota01 = float(input("Digite a nota 01: "))
nota02 = float(input("Digite a nota 02: "))
nota03 = float(input("Digite a nota 03: "))

media = calcular_media(nota01, nota02, nota03)
situacao = verificar_situacao(media)

print(f"O aluno {nome} teve média {media:.2f}")