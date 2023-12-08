'''
El usuario ingresa su año de nacimiento.
La máquina calcula y muestra su edad aproximada.
'''

# Entrada --> Proceso --> Salida

anio_actual = 2023

# Entrada
anio_de_nacimiento = int(input("¿En que año naciste? "))

# Proceso
edad = anio_actual - anio_de_nacimiento

# Salida
# Concatenar usando varios parámetros en el print() (Sólo sirve para el print)
print("Tu edad es de",edad,"ó",(edad-1),"años")

# Concatenar usando el + (Sólo para string)
print("Tu edad es de " + str(edad) + " ó " + str(edad-1) + " años")

# Concatenar con Interpolación de String
print(f"Tu edad es de {edad} ó {edad-1} años")