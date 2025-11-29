'''correo = input()

if correo.count('@') > 1:
    print(False)
elif ' ' in correo:
    print(False)
elif correo.startswith('.') or correo.endswith('.'):
    print(False)
elif '.' not in correo:
    print(False)
    
else:
    Partes = correo.split('@')
    if len(Partes[0]) <3 or len(Partes[1]) <3 :
        print(False)
    else: 
        print(True)'''

'''cadena = input().lower()
letra = cadena.count('z')
if letra >= 1:
    print(f'En la cadena {cadena} aparecen {letra} letras z')
elif letra == 0:
    print(f'En la cadena {cadena} no aparece ninguna z')'''
    

'''x= int(input())
a= input()
b= input()

parte1 = a[:len(a)//x]
parte2 = b[-(len(b)//x):]
print(parte1+parte2)'''

'''a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a*b)-(c*d))'''

'''nota1 = float(input())
nota2 = float(input())
nota3 = float(input()) 
nota4 = float(input())
nota5 = float(input())
nota6 = float(input())

Notas = [nota1, nota2, nota3, nota4, nota5, nota6]

print(f'Maximo: {max(Notas):.2f}')
print(f'Minimo: {min(Notas):.2f}')
print(f'Diferencia: {max(Notas)-min(Notas):.2f}')
print(f'Suma: {sum(Notas):.2f}')
print(f'Promedio: {sum(Notas)/len(Notas):.2f}')'''


'''nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
nota4 = int(input())
nota5 = int(input())

porcentaje1= float(input())
porcentaje2= float(input())
porcentaje3= float(input())
porcentaje4= float(input())
porcentaje5= float(input())

total = (nota1*porcentaje1 + nota2*porcentaje2 + nota3*porcentaje3 + nota4*porcentaje4 + nota5*porcentaje5) 
print(int(total))'''

'''nombre = input()
apellido = input()

nick= nombre[:5] + apellido[0]
nick = nick.lower()
pin = (len(nombre)* 1000 + len(apellido)) % 10000
idd= 'C3-' + nick + '-' + str(pin)

print(f'Nick: {nick}')
print(f'Pin: {pin}')
print(f'ID: {idd}')'''

'''fecha = input()
dia,mes,año = fecha.split('/')
formato = año + '/' + mes + '/' + dia 
print(formato)'''

'''platos_principales =('Hamburguesa', 'Pizza', 'Tacos', 'Pupusas', 'Hotdog')
complementos = ('Papas fritas', 'Alitas de pollo', 'Ensaladas', 'Sopa', 'Lasaña')

num1 = int(input())
num2 = int(input())

print(f'El pedido de Alvin es: {platos_principales[num1-1]} con {complementos[num2-1]}')'''


num =int(input())

suma = num*(num+1)/2
print(suma)
