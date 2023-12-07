from random import randint
import os
import time
tablero = []

for a in range(3):
    tablero.append(["O"] * 3)

def MostrarTablero(tablero):
    print("  A B C ")
    for i, fila in enumerate(tablero, start=1):
        print(i, " ".join(fila))

def letra_a_numero(letra):
    return ord(letra.upper()) - ord('A')

def numero_a_letra(numero):
    return chr(numero + ord('A'))

def random_numero(tablero):
    return randint(0, len(tablero) - 1)

def random_letra(tablero):
    return randint(0, len(tablero[0]) - 1)

barco_numero = random_numero(tablero)
barco_letra = random_letra(tablero)

print ("Bienvenido a ⚓​ Battleshippp ⚓")
input("Presiona ENTER para continuar ")

for turn in range(9):
    os.system("cls")
    print("Estas en el turno : ", turn + 1)
    MostrarTablero(tablero)
    letra = input("LETRA:")
    numero = int(input("NUMERO:")) -1 # SIN EL MENOS 1 SELECCIONARA LA LINEA DE ABAJO DEL TABLERO
    guess_col = letra_a_numero(letra)

    if numero == barco_numero and guess_col == barco_letra:
        print("Felicidades! has destruido mi barco!")
        input()

        break
    else:
        if (numero < 0 or numero > 5) or (guess_col < 0 or guess_col > 5):
            print("Eso ni siquiera esta en el tablero 🎲.")
        elif(tablero[numero][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("has fallado!")
            tablero[numero][guess_col] = "X"
            input()
            os.system("cls")
    if turn == 8:
        print("Game Over")
