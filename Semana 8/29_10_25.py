'''ejecucion = True

while ejecucion:
    opcion = input('Continuamos ejecutando el menu? Y/N:')
    if opcion.lower() == 'n':
        ejecucion = False
    elif opcion.lower() == 'y':
        print ('Ok, continuemos')
    else:
        print('La opcion elegia no es valida')
        
print('Gracias por utilizar nuestro sistema!!!')


#un pequeño sistema de registro de alumnos#
#configuracion inicial#

alumnos = 0
lista_alumnos = []

alumno = input('Digite el nombre del pajarito: ')
lista_alumnos.append(alumno)

print(lista_alumnos)'''

menu_activo = True
while menu_activo:
    opcion = input('Elija la opcion (1: ingresar alumno, 5: Salir): ')
    if opcion == '5':
        menu_activo = False
    elif opcion == '1':
        alumno = input('Nombre del alumno agregar: ')
        lista_alumnos.append(alumno)
    elif opcion == '2':
        print(lista_alumnos)
    elif opcion == '3':
        i = int(input('Ingrese la posicion del alumno a modificar: '))
        n = input('Ingrese el nuevo nombre del alumno: ')
        lista_alumnos[i-1] = n
    elif opcion == '4':
        borrado = lista_alumnos.pop(int(input('Ingrese el numero del alumno a popear (1-4):'))-1)
        print(f'Usted ha popeado a {borrado}.')
print('Gracias por utilizar nuestro sistema.')
