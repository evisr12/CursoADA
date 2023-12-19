import os

laberinto = [
    "##########",
    "#P.......#",
    "#.#######.#",
    "#.#.......#",
    "#.#.#####.#",
    "#.#.#.....#",
    "#.#.#.###.#",
    "#...#.....#",
    "#.#######.#",
    "##########"
]

posicion_personaje = [1, 1]

def imprimir_laberinto():
    os.system("clear" if os.name == "posix" else "cls")
    for fila in laberinto:
        print(fila)

# Solicitar el nombre del jugador
nombre_jugador = input("¡Bienvenido! Por favor, ingresa tu nombre: ")

# Mostrar mensaje de bienvenida
print(f"\n¡Hola {nombre_jugador}! Bienvenido al juego del laberinto.\n")

while True:
    imprimir_laberinto()

    direccion = input("Muevete con las flechas del teclado (↑, ↓, ←, →). Presiona 'q' para salir: ").lower()

    if direccion == "q":
        break
    elif direccion == "\x1b[A" and laberinto[posicion_personaje[0] - 1][posicion_personaje[1]] != "#":
        laberinto[posicion_personaje[0]][posicion_personaje[1]] = "."
        posicion_personaje[0] -= 1
    elif direccion == "\x1b[B" and laberinto[posicion_personaje[0] + 1][posicion_personaje[1]] != "#":
        laberinto[posicion_personaje[0]][posicion_personaje[1]] = "."
        posicion_personaje[0] += 1
    elif direccion == "\x1b[C" and laberinto[posicion_personaje[0]][posicion_personaje[1] + 1] != "#":
        laberinto[posicion_personaje[0]][posicion_personaje[1]] = "."
        posicion_personaje[1] += 1
    elif direccion == "\x1b[D" and laberinto[posicion_personaje[0]][posicion_personaje[1] - 1] != "#":
        laberinto[posicion_personaje[0]][posicion_personaje[1]] = "."
        posicion_personaje[1] -= 1

    laberinto[posicion_personaje[0]][posicion_personaje[1]] = "P"
