import os
from time import sleep
from random import randint

def animacion_disparo():
    for i in range(5):
        limpiar_pantalla()
        print("\033[1;31m¡Fuego enemigo!\033[0m")
        print(" " * i + "\033[1;32m▶\033[0m")
        sleep(0.3)

def animacion_seleccion():
    for _ in range(4):
        limpiar_pantalla()
        print("Estás eligiendo la posición...")
        sleep(0.5)

def mostrar_tablero(tablero):
    print("  A B C D ")
    for i, fila in enumerate(tablero, start=1):
        print(i, " ".join(fila))

def letra_a_numero(letra):
    return ord(letra.upper()) - ord('A')

def numero_a_letra(numero):
    return chr(numero + ord('A'))

def validar_letra(letra):
    return letra.upper() in ['A', 'B', 'C', 'D']

def validar_numero(numero, tamaño_tablero):
    return 1 <= numero <= tamaño_tablero

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
