cadena = input('Ingrese una cadena: ')
print(cadena[::-1])

caracter = input('Ingrese un caracter: ')
contador = 0

for i in range(len(cadena)):
    if cadena[i] == caracter:
        contador += 1

print('El caracter se repite:' , contador, 'veces.')


cadena2 = input('Ingrese una cadena: ')
distanciaHamming = 0

if len(cadena) == len(cadena2):
    for i in range(len(cadena)):
        if cadena[i] != cadena2[i]:
            distanciaHamming += 1
    print('Distancia es de: ')
else:
    print('Cadenas de distinta longitud.')

