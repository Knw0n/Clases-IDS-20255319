#trabajando con listas #

'''datos = [1,2,"tres",["lunes","martes","miercoles"]]
print((datos[2])[1])
print((datos[3])[2][3])'''

import os


numeros = ['uno','dos','tres']
print(numeros)
numeros = numeros + ['cuatro','cinco', 'seis']      #concatenacion de listas #
print(len(numeros))

numeros[2] = 'trois'
print(numeros)
numeros.append(input("Escrina el siente numero: "))    #agregar un elemento al final de la lista #
print(numeros)

numeros.insert(2, input("Escriba el nuevo elemento: "))    #agregar un elemento en una posicion especifica #