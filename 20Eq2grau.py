# Exercício 20
# Receba os coeficientes A, B e C de uma equação do 2º grau.
# Verifique a existência de raízes reais e, se existirem, calcule-as.

# Declarar variáveis globais
a = 0.0
b = 0.0
c = 0.0
delta = 0.0
x1 = 0.0
x2 = 0.0


def calcular_raizes():
    global a, b, c, delta, x1, x2

    # Processamento
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x1 = -b / (2 * a)
        print("Existe uma raiz real.")
        print("Raiz:", x1)
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)

        print("Existem duas raízes reais.")
        print("X1:", x1)
        print("X2:", x2)


def main():
    global a, b, c

    # Entrada de dados
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    calcular_raizes()


main()