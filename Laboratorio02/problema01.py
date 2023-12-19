# Solicitar la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

# Mostrar el precio de la entrada al usuario
print("El precio de la entrada es:", precio, "monedas.")