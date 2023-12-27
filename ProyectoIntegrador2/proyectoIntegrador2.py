#1. Instalar readchar: pip install readchar

#improtar librería readchar

import readchar

print("Presiona las teclas. Presiona la tecla ↑ para salir.")

while True:
    key = readchar.readkey()
    print(f'Tecla presionada: {key}')

    # Verifica si la tecla presionada es la tecla de flecha hacia arriba (UP)
    if key == '\x1b[A':
        print("Tecla de flecha hacia arriba presionada. Saliendo del programa.")
        break

