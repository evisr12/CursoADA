# 1. Crea un nuevo archivo .py

# 2. Define una variable de cada tipo primitivo

# Entero (int)
entero = 10

# Punto flotante (float)
flotante = 3.14

# Cadena de texto (str)
cadena = "Hola, mundo!"

# Booleano (bool)
booleano = True

# Lista
lista = [1, 2, 3, 4, 5]

#2.1 Concatenar variables a la cadena original
resultado_concatenacion = cadena + " " + str(entero) + " " + str(flotante) + " " + str(booleano) + " " + str(lista)

#2.2 Investigar
# Limite de los enteros en Python
# En Python, el tamano de los enteros esta limitado por la arquitectura de la maquina.
# En sistemas de 32 bits, el rango es aproximadamente de -2**31 a 2**31 - 1.
# En sistemas de 64 bits, el rango es mucho mas grande, de -2**63 a 2**63 - 1.

# Limite de los flotantes en Python
# Los numeros de punto flotante en Python siguen el estandar IEEE 754.
# En general, tienen una precision finita y no pueden representar todos los numeros reales de forma exacta.
# El limite de precision se hace evidente al realizar operaciones aritmeticas con numeros muy grandes o muy pequenos.

#2.3
n = 5  # Se puede cambiar este valor
# Aplicar la formula
suma_pares = n * (n + 1)

#2.4 Resultados
# variables primitivas
print("Entero:", entero)
print("Punto flotante:", flotante)
print("Cadena de texto:", cadena)
print("Booleano:", booleano)
print("Lista:", lista)

# Concatenacion
print("Resultado de la concatenacion:", resultado_concatenacion)

# suma de n pares
print("La suma de los primeros", n, "numeros pares es:", suma_pares)