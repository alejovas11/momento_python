flag = 1
listaNumeros = []

while flag != 0:
    
    numbers = int(input('Ingrese un numero: '))

    if numbers == 0:
        flag = 0
    else:
        listaNumeros.append(numbers)


ordenados = sorted(listaNumeros)
print('Lista ordenada')
print(ordenados)