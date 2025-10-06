
#validar el usuario

#Mostrar menus segun usuario

#defininir tareas para usuario

#Presentar resumenes del usuario

usuario = "Alvin" #Tipo string
cantidad_alumnos = 79 
media_edad = 18.231234
monto_hope = 1234567.8901
inversion_evento = -98765.21548

print (type(cantidad_alumnos))
print (type(media_edad))

#Print and validate variable

print(type(cantidad_alumnos)is int)  #no es lo mismo a la expresion "int". int =/ a "int"
print(type(media_edad)is int)  #no es lo mismo a la expresion "int". int =/ a "int"

""" Un algoritmo produce una entrada y una salida, realiza una serie de pasos ordenados y finitos 
y nos resuelve un problema. "Type" es una funcion que retorna el tipo de dato de la variable que 
yo estoy propocionando""" 

print ("el usuario es", usuario, "y tiene", cantidad_alumnos, "pajaritos en su aula")
print ("la edad promedio es de", media_edad)

""" f-strings: son cadenas de texto que permiten incrustar expresiones dentro de llaves {}.
Viene de string (texto), pero es texto formateado"""

print (f"El usuario es {usuario}")
print(f"y en su auala con {cantidad_alumnos-4} parajitos") # EL f-string permite hacer operaciones dentro de las llaves, junto con el/los variables
print(f"con edad promedio de {media_edad:.1f} años") # El variable se puede ser modificado. En este caso, se limita a 1 decimal usando ".1f", 1=cantidad de decimales, f = float, o puesto fijo. "." = separador decimal
print(f"colectaron ${monto_hope:,.2f} como un donativo.")  # Hablando de cantidades en miles. , = separador de miles, .2f = 2 decimales
print(f"y la totalidad de gastos fue de ${abs(inversion_evento):,.2f}") # abs = valor absoluto

print(type(usuario) is str)

esta_lloviendo = False
print(type(esta_lloviendo) is bool) #bool = booleano, es decir, verdadero o falso (1 o 0).
print(type(monto_hope) is not bool) #En este caso, se niega que monto_hope sea booleano.


nombre = "Alvin"
apellido = "Portillo"
nombre_completo = nombre + " " + apellido  #Concatenacion de strings. Solo se puede concatenar strings con strings, no con otros tipos de datos.
print(nombre_completo)

""" Python es un lenguaje de tipado dinamico, es decir, no es necesario declarar el tipo de dato 
de una variable al momento de crearla."""
