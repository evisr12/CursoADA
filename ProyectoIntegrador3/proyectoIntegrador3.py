import os

def clear_terminal():
    # Borra la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Inicializa el número en 0
    numero = 0

    print("Presiona la tecla e para incrementar el número. Presiona cualquier otra tecla para salir.")

    while numero <= 50:
        clear_terminal()  # Limpia la terminal
        print(f"Número actual: {numero}")

        # Lee la tecla presionada
        tecla = input()

        # Verifica si la tecla presionada es 'e'
        if tecla.lower() == 'e':
            numero += 1
        else:
            break  # Sale del bucle si se presiona cualquier otra tecla

if __name__ == "__main__":
    main()
