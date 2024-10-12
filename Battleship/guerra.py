from funciones import *
from random import randint

# Constantes del juego
tamaño_tablero = 4
turnos_maximos = 3

tablero = [["O"] * tamaño_tablero for _ in range(tamaño_tablero)]
barco_numero = randint(0, tamaño_tablero - 1)
barco_letra = randint(0, tamaño_tablero - 1)

print("Bienvenido a ⚓​ Battleshippp ⚓\n")
input("Presiona ENTER para continuar ")

for turn in range(turnos_maximos):
    limpiar_pantalla()
    print("Estás en el turno:", turn + 1)
    mostrar_tablero(tablero)

    letra = input("LETRA: ")
    while not validar_letra(letra):
        print("Entrada no válida. Introduce una letra válida (A, B, C, D).")
        letra = input("LETRA: ")

    numero = int(input("NUMERO: ")) - 1
    while not validar_numero(numero + 1, tamaño_tablero):
        print("Entrada no válida. Introduce un número válido (1, 2, 3, 4).")
        numero = int(input("NUMERO: ")) - 1

    barcoenemigo = letra_a_numero(letra)

    animacion_seleccion()
    animacion_disparo()

    if numero == barco_numero and barcoenemigo == barco_letra:
        print("¡Felicidades! ¡Has destruido mi barco!")
        input()
        break
    else:
        print("¡Has fallado!")
        tablero[numero][barcoenemigo] = "X"
        input()

    if turn == turnos_maximos - 1:
        input("Juego terminado. No has destruido mi barco.")
    limpiar_pantalla()
