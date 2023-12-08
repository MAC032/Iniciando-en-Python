"""
mensaje = "Ingrese número positivo "

num = int(input(mensaje))
while num <= 0:
    num = int(input(f"ERROR. {mensaje}"))
    # Otra operación
print("Seguimos adelante con un numero positivo")
"""
# En Python no hay do-while

for i in range(10):
    # print(i)
    # print(i, end = " ")
    # print(i, end = " , ")
    print(i, end = "\t")
print()
for i in range(1, 11):
    print(i, end = " ")
print()
for i in range(1, 11, 2):
    print(i, end = " ")