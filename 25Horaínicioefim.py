# Declarar variáveis globais
hora_inicio = 0
minuto_inicio = 0
hora_final = 0
minuto_final = 0
duracao = 0
horas = 0
minutos = 0


def calcular_tempo():
    global hora_inicio, minuto_inicio, hora_final, minuto_final
    global duracao, horas, minutos

    # Transformar os horários em minutos
    inicio = hora_inicio * 60 + minuto_inicio
    final = hora_final * 60 + minuto_final

    # Verificar se terminou no dia seguinte
    if final <= inicio:
        final = final + 24 * 60

    # Calcular duração
    duracao = final - inicio

    horas = duracao // 60
    minutos = duracao % 60

    # Mostrar resultado
    print("Duração do jogo:", horas, "hora(s) e", minutos, "minuto(s)")


def main():
    global hora_inicio, minuto_inicio, hora_final, minuto_final

    # Entrada de dados
    hora_inicio = int(input("Hora de início: "))
    minuto_inicio = int(input("Minuto de início: "))

    hora_final = int(input("Hora final: "))
    minuto_final = int(input("Minuto final: "))

    calcular_tempo()


main()