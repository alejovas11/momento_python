names = []
nombresConC = []
i = input("Desea ingresar un nuevo nombre: SI / NO ")
j= i.upper()


while j == "SI":
    nombre = input("Ingrese el nombre: ")

    names.append(nombre)

    i = input("Desea ingresar un nuevo nombre: SI / NO ")
    j = i.upper()
for x in names:
    if x[0] == 'C' or x[0] == 'c':
        nombresConC.append(x)

lNombresConC = ', '.join(nombresConC)       

print(f"Los nombres que contienen la C son: {lNombresConC}")