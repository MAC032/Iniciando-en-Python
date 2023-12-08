llueve = True
if llueve:
    print("Llevar paraguas")

edad = 26
EDAD_LEGAL = 18

if edad >= EDAD_LEGAL:
    print("Pasa")
else:
    print("NO Pasa")
print("Chau")

num = 4
if num > 0:
    print("Positivo")
else:
    if num < 0:
        print("Negativo")
    else:
        print("Neutro")

if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Neutro")

numero_marcado_en_telefono = 4
match numero_marcado_en_telefono:
    case 1:
        print("Ventas")
    case 2:
        print("RRHH")
    case _:
        print("ERROR")

