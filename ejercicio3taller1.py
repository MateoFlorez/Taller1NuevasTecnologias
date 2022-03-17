opcion = 1
contador = 1
numeros = []

print('MENÚ DEL PROGRAMA')
print('1. Recibir 5 números')
print('2. Sumar números ingresados')
print('3. Agregar un nuevo número')
print('4. Salir')

while (opcion != 4):
    opcion = int(input('Digita una opción: '))
    if (opcion == 1):
        while (contador <= 5):
            numero = int(input('Digita un numero: '))
            numeros.append(numero)
            print(numeros)
            contador += 1
    elif (opcion == 2):
        suma = sum(numeros)
        print(f'La suma es: {suma}')
    elif (opcion == 3):
        numero = int(input('Digita un nuevo nuevo: '))
        numeros.append(numero)
        print(numeros)
    elif (opcion == 4):
        print('Saliendo del programa')
    else:
        print('Digita una opción válida')
else:
    print('---------------------------------------')
    print('Saliste del programa.')