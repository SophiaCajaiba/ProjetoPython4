# Exercício 21
# Receba 4 notas bimestrais.
# Calcule a média e mostre a situação do aluno.

# Declarar variáveis globais
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
media = 0.0


def calcular_media():
    global nota1, nota2, nota3, nota4, media

    # Processamento
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Mostrar resultado
    print("Média:", media)

    if media >= 6:
        print("APROVADO")
    elif media >= 3:
        print("EXAME")
    else:
        print("RETIDO")


def main():
    global nota1, nota2, nota3, nota4

    # Entrada de dados
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    calcular_media()


main()