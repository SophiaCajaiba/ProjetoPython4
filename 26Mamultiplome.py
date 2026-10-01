# Declarar variáveis globais
numero1 = 0
numero2 = 0
maior = 0
menor = 0


def verificar_multiplo():
    global numero1, numero2, maior, menor

    # Processamento
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1

    # Mostrar resultado
    if maior % menor == 0:
        print("O maior número é múltiplo do menor.")
    else:
        print("O maior número não é múltiplo do menor.")


def main():
    global numero1, numero2

    # Entrada de dados
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    verificar_multiplo()


main()