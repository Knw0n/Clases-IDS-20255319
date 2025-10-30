nombres = ["Ana", "Antonio", "Ana", "Jose"]

'''print(nombres.count("Jose"))
r_a = 0
print(nombres.count("Maria"))
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a)

print(nombres.index("Ana",1))  #buscar la posicion de un elemento en la lista a partir de una posicion especifica #

int(nombres.index('Ana',nombres.index('Ana')+1))  #buscar la posicion de la segunda ocurrencia de un elemento en la lista #
'''

nombres = ["Ana", "Antonio", "Ana", "Jose", 'Carlos']
'''print(nombres.append('Aby'))
print(nombres)
nombres.insert(int(input('Posicion:')), input('Nombre Nuevo:')) #insertar un elemento en una posicion especifica #
print(nombres)'''

'''nombres[int(input('Posicion:'))] = input('Nombre Nuevo:') #insertar un elemento en una posicion especifica #
print(nombres)

nombres.remove('Ana')   #eliminar la primera ocurrencia de un elemento en la lista #

nombre_borrado = nombres.pop(3)
print(f'Nombre borrado: {nombre_borrado}') #almacenar el elemento eliminado en una variable #

nombres.reverse()
print(nombres)

#herramientas de control de flujo#'''

'''numero = 6
captura = int(input('Adivina el numero (un intento): '))
if captura == numero:
    print('Le acertaste!')
print('Puedes seguir jugando')

nota = int(input('Escribe tu nota: '))
if nota >= 8:
    print('Excelente!')
elif nota >= 6:
    print('Bueno!')
elif nota >= 4:
    print('Regular!')
    
else:
    print('Malo!')
'''
#23/10/25#

'''monto = int(input('Monto a pagar: '))
tipo = input('Tipo (local/internacional): ')
impuesto = 0

if tipo.lower() == 'local':
    if monto >= 100:
        impuesto = 0.07
    else:
        if monto >= 75:
            impuesto = 0.05
        else:
            impuesto = 0
elif tipo.lower() == 'internacional':
    if monto >= 100:
        impuesto = 0.12
    elif monto >= 75:
        impuesto = 0.10
    else:
        impuesto = 0

else:
    print('Ese tipo no existe')
print(f'El tipo {tipo} con monto {monto:,.2f}')
print(f'paga un impuesto de {monto*impuesto:.2f}%')'''

#Iteraciones#
nombre = ['Ana', 'Jose', 'Luis']

for x in nombre:
    print(f'Hola {x}')

