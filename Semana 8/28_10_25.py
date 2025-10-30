'''palabra = 'hola'
print(len(palabra))

lista = [10, 20, 30, 40, 50]
print(len(lista))

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
print(len(dias))

for i in dias:          # i es iterador, toma cada valor de la lista dias, dias siendo el iterable#
    print('Hola profe')
    
for i in palabra:
    print(i)
    

#for i in dias#

for i in range(5):
    print('Buenos dias')

for i in dias[3]:
    print(i)
    
    
valores = [[1,2,6], [2,7,4], [6,5,9], [1,10,20]]

for i in valores:
    for j in i:
        if j > 6:
            print(j) 

mayores = []
for v in valores: 
    for i in v:
        if i>6:
            mayores.append(i)

print(mayores)'''

#while#

'''limite = 8
inicio = 0 
while inicio < limite:
    print(inicio)
    inicio = inicio + 1 
    '''

presupuesto = 1000
gasto = 0 

while gasto < presupuesto:
    compra = float(input('Monto a comprar: '))
    gasto += compra
gasto -= compra
print('Se ha llegado al limite del presupuesto')
print(f'El monto gastado es de {gasto:,.2f}')