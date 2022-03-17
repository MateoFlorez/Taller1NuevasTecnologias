contador = 1
multiplo3 = 0
multiplo2 = 0

while (contador <= 5):
    numero = int(input('Digite un numero: '))
    if (numero % 2 == 0):
        multiplo2 += 1
    elif (numero % 3 == 0):
        multiplo3 += 1
    contador += 1

print(f'Cantidad de multiplos de 2: {multiplo2}')
print(f'Cantidad de multiplos de 3: {multiplo3}')