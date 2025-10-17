""" EJERCICIO A
Te han asignado la misión de crear este nuevo programa. 
Tu programa debe recibir un correo a validar e imprimir un mensaje que indique si es válido o 
inválido (True/False). Para que un correo se considere válido, debe cumplir las siguientes 
condiciones:

1. El correo contiene exactamente un @
2. Antes y después del @ debe haber al menos 3 caracteres
3. El correo debe contener al menos un punto
4. El correo no puede contener espacios
5. El correo no puede iniciar ni terminar con un punto

correo = input()
r1 = correo.count("@") == 1 
if r1: 
    usuario, dominio = correo.split("@")
    r2 = len(usuario) >=3 and len(dominio) >= 3
else: 
    r2 = False
r3 = correo.count(".") >= 1
r4 = correo.count(" ") == 0
r5_1 = correo[0] != "."
r5_2 = correo[-1] != "."


restricciones = r1 and r2 and r3 and r4 and r5_1 and r5_2
print(restricciones)"""

##################################################

""" EJERCICIO B 

Enunciado

Un dragón duerme sobre una cadena de letras. Para que no despierte, debes contar cuántas veces aparece la letra z en la cadena.

Entrada:

Una cadena de hasta 100 caracteres en minúsculas.
Salida:

Un número entero con la cantidad de letras z.

cadena = input().lower()

letra = cadena.count("z")

print(letra) """

###################################################

""" EJERCICIO C 
En la ESEN, estamos experimentando demasiados problemas con las contraseñas. Esta vez, 
la víctima es el pobre OOF.
Al igual que con la contraseña de Alvin, Issem es el malandro que ha hackeado y encriptado la 
contraseña de Steam de OOF. No obstante, esta vez no se llegó a un acuerdo con el Señor Oscuro, 
por lo que podemos esperar que la recuperación de la contraseña no será tan sencilla como la vez 
pasada.
Afortunadamente, con la ayuda del coco de Rober Polanski, hemos sido capaces de descifrar la 
forma de recuperar la contraseña, siendo así:

1. Polanski encontró 2 palabras escondidas (A y B).
2. La primera parte de la contraseña, son los primeros |A|/X caracteres de A, donde |A| 
   representa el tamaño de la cadena A.
3. La segunda parte de la contraseña, son los últimos |B|/X caracteres de B, donde |B| 
   representa el tamaño de la cadena B.

¿Puedes ayudar a que OOF recupere su cuenta de Steam?

Entrada
La primera línea contiene un único entero X, los caracteres que tienes que tomar en cuenta. 
La segunda línea presenta una cadena de caracteres A. La última línea contiene una cadena de 
caracteres B.

Salida
Imprime una única cadena de caracteres, la contraseña recuperada

Restricciones
El tamaño de A y B siempre será a lo sumo 100 caracteres X siempre será un divisor del tamaño 
de A y B, aunque dichas cadenas no tengan el mismo tamaño.

x = int(input())
A = input()
B = input()

len_A = int(len(A)/x)
len_B = int(len(B)/x) 

parte_A = A[:len_A]
parte_B = B[-len_B:]

contraseña = parte_A + parte_B
print(contraseña)
"""

###################################################

"""EJERCICIO D
Descripción
Lea cuatro enteros A, B, C y D. Calcule e imprima la diferencia del producto A y B con el 
producto C y D, es decir, calcule (A * B - C * D).

Entrada
Cuatro enteros A, B, C y D.

Salida
Imprima la diferencia, es decir, (A * B - C * D).

A = int(input())
B = int(input())
C = int(input())
D = int(input())

product =  (A*B) - (C*D)

print(product)
"""

###################################################

"""EJERCICIO E

Alvin le pidió a sus ayudantes favoritos (ya los conoces) que le entregaran un reporte acerca 
del desempeño de los estudiantes de Introducción al Desarrollo de Software.

Ellos ya calificaron, pero están demasiado ocupados en sus otras actividades, como organizar 
competencias, escribir problemas y debatir sobre Kirby. Por eso necesitan tu ayuda para generar 
el resumen estadístico automáticamente.

Entrada
Recibirás 6 datos de tipo float, cada uno en una línea independiente.

Estos representan las notas de los estudiantes ya calificadas. Puedes usar una lista para 
almacenarlas.

Salida
Debes calcular y mostrar en líneas separadas lo siguiente, con formato de 2 decimales en todos 
los valores numéricos:

1. El máximo
2. El mínimo
3. La diferencia entre el máximo y el mínimo
4. La suma total de las 6 notas
5. El promedio de las 6 notas
6. Cada línea debe seguir estrictamente el formato indicado:

La palabra del campo (escríbela exactamente igual), seguida de dos puntos, un espacio y el 
número con dos decimales. Presta mucha atención a las mayúsculas, los acentos y los espacios, 
ya que cualquier diferencia hará que tu programa no produzca la salida correcta.

Nota: El orden de las líneas es obligatorio y el formato de dos decimales debe aplicarse 
incluso a los números enteros para mantener la coherencia.


nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())
nota_4 = float(input()) 
nota_5 = float(input())
nota_6 = float(input())

notas = [nota_1, nota_2, nota_3, nota_4, nota_5, nota_6]
max = max(notas)
min = min(notas)

print (f"Maximo: {max:.2f}")
print (f"Minimo: {min:.2f}")
print (f"Diferencia: {(max - min):.2f} ")
print (f"Suma: {sum(notas):.2f}")
print (f"Promedio: {sum(notas)/len(notas):.2f} ")

"""

###################################################

""" EJERCICIO F

Contexto
La primera ronda de la Copa Salvadoreña de Programacion ha llegado a su fin. El jurado estaba a 
punto de revisar los resultados del equipo NESE, pero el internet dejo de funcionar!

Afortunadamente, Crijeme tiene anotado cuantos puntos otorga cada problema y el porcentaje de 
los puntos que obtuvo el equipo para cada problema.

Ayuda a determinar cual es el total de puntos que logro el equipo NESE si la competencia 
consistio de 5 problemas.

Entrada
Vas a recibir 10 numeros en total.

Los primeros 5 numeros enteros determinan la cantidad de puntos que otorga cada problema.

Los ultimos 5 numeros decimales detereminan el porcentaje que obtuvo cada equipo.

Salida
Un solo numero entero que indique la puntuacion total del equipo NESE.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

puntos = [a, b, c, d, e]

f = float(input())
g = float(input())
h = float(input())
i = float(input())
j = float(input())

porcentaje = [f, g, h, i, j]

total = (puntos[0] * porcentaje[0]) + (puntos[1] * porcentaje[1]) + (puntos[2] * porcentaje[2]) + (puntos[3] * porcentaje[3]) + (puntos[4] * porcentaje[4])

print(total)
"""

###################################################

""" EJERCICIO G 

Mientras él escribe los problemas para la próxima Copa Salvadoreña de Programación, te ha 
encargado algo muy importante: el sistema de creación de usuarios y cuentas para las 
competencias del C3.

Entrada
Recibirás 2 cadenas (strings), una por línea:

El nombre del competidor, que siempre tendrá al menos 5 caracteres (garantizado).
El apellido del competidor.
Procesamiento
Con estos datos, deberás construir la cuenta siguiendo las indicaciones del presi, ChrisM:

Nick: Toma los primeros 5 caracteres del nombre, agrega el primer carácter del apellido, y 
convierte todo a minúscula.

Pin: Calcula el pin como:

len(nombre) * 1000 + len(apellido)

Luego aplícale un módulo 10000 (% 10000) para mantenerlo en 4 dígitos.

ID: Une las partes con el formato: "C3-" + nick + "-" + pin 

nombre = input()
apellido = input() 

nick = nombre[:5] + apellido[0]
nick = nick.lower()

pin = (len(nombre) * 1000 + len(apellido)) % 10000

ID = "C3-" + nick + "-" + str(pin)

print(f"Nick: {nick}")
print(f"Pin: {pin}")
print(f"ID: {ID}" 

"""

###################################################

"""EJERCICIO H 
Como bien sabrás, los Autovengadores tenemos sedes por todo el mundo.

En esta ocasión, al enviar información a la sede de Estados Unidos, el Profe Pleités se ha 
olvidado de ajustar ciertos datos para una mejor comprensión, por ejemplo, la fecha.

Nosotros utilizamos el formato de DD/MM/YYYY, mientras que ellos usan el formato YYYY/MMM/DD
¿Puedes diseñar un algoritmo que realice el cambio?

Entrada
La única línea de entrada contiene una cadena F, la fecha en formato DD/MM/YYYY

Salida
Imprime una sola cadena, la fecha en formato YYYY/MMM/DD


Restricciones
La cadena F estará siempre en formato DD/MM/YYYY

cadena = input()

dia, mes, año = cadena.split('/')

formato = año + "/" + mes + "/" + dia

print(formato)"""

###################################################

""" EJERCICIO I

Indicaciones
Alvin lleva mucho tiempo siendo cliente frecuente del programa de pedidos y ya es costumbre que 
todos los días que sale noche de la ESEN pide su cena usándolo. Pero después de tanto tiempo, 
Alvin se ha cansado de solo poder pedir un plato por orden, ya que a veces se queda con hambre 
y no se llena por completo.

Para mejorar la experiencia de Alvin, sus estudiantes han decidido actualizar el programa para 
permitir que pueda pedir un plato principal y un complemento. Con el fin de lograr esto, el 
menú del programa ahora estará organizado en dos tuplas. Una para los platos principales y otra 
para los complementos. El menú actualizado es el siguiente:

Platos principales:
1. Hamburguesa
2. Pizza
3. Tacos
4. Pupusas
5. Hotdog

Complementos:
1. Papas fritas
2. Alitas de pollo
3. Ensalada
4. Sopa
5. Lasaña

Tu misión es realizar las modificaciones necesarias para lograr que Alvin pueda ordenar un 
plato principal y un complemento juntos. El programa deberá recibir dos números enteros:

El número del plato principal dentro del menú
El número del complemento dentro del menú
Luego, el programa debe imprimir un mensaje que muestre el pedido completo de Alvin, con el 
formato:

El pedido de Alvin es: (Plato) con (Complemento)
Entrada
Dos números enteros:

El número del plato principal dentro del menú
El número del complemento dentro del menú
Salida
Una línea con el mensaje:

El pedido de Alvin es: (Plato) con (Complemento)
donde (Plato) corresponde al nombre del plato principal seleccionado por Alvin y (Complemento) 
corresponde al nombre del complemento elegido.

principales = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
completos = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")

numero_1 = int(input())
numero_2 = int(input())

orden_1 = principales[(numero_1)-1]
orden_2 = completos[(numero_2)-1]

print(f"El pedido de Alvin es: {orden_1} con {orden_2}")

"""

###################################################

"""EJERCICIO J 

Contexto
"TLE otra vez!" Exclamo Polanski mientras experimentaba con bucles y matematicas. Cansado de 
complicarse la vida, decidio realizar un problema diferente:

Dado un numero N, cual es la suma de los numeros enteros desde 1 hasta N ?

Debido a su odio (temporalmente) por los bucles, ha decidido resolver este problema sin 
utilizar ninguna forma de bucles. Para poder hacer esto, el Profe Pleites, al que le daban 
FosfoNeuroMAX de pequeño, le entrego a Polanski la siguiente formula:

Para obtener la suma, debes multiplicar el numero N por su consecutivo proximo y dividir el 
resultado entre 2

Utiliza la formula y ayuda a Polanski a encontrar la suma sin utilizar bucles.

Entrada
Un unico numero entero N

Salida
La suma de los numeros desde 1 hasta N

N = int(input())

producto = int((N * (N+1))/2)

print(producto)

"""

###################################################

"""EJERCICIOS DE CONTROL2"""

###################################################

"""EJERCICIO C 

menu = ("Hamburgesa", "Hotdog", "Pizza", "Taccos", "Lasaña", "Ensalada", "Pupusas", "Burrito", "Alitas de pollo", "Papas fritas")

precios = [3.52, 55.15, 4.25, 60.25, 5.65, 3.15, 2.65, 70.75, 6.25, 2.55]

numero = int(input())
nuevo_precio = float(input())

precios[(numero)-1] = nuevo_precio

print(f"Los precios actualizados son: [{precios}]")"""

###################################################

"""EJERCICIO D

correo = input()

veri_1 = correo.count('@') == 1
veri_2 = correo[0] != "@"
veri_3 = correo[:-1] != "@"

print (f" Contiene exactamente un @: {veri_1}")
print(f"El @ no está ubicado al inicio del correo: {veri_2}")
print(f"El @ no está ubicado al final del correo: {veri_3}")

"""

###################################################

"""EJERCICIO E

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

nota_final = float((n1*.15) + (n2*.4) + (n3*.25) + (n4*.20) + (n5*.05))

print(f"La nota final es: {nota_final:.2f}")"""