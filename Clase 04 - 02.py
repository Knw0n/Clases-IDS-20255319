cantidad_alumnos = 25
nombre_profe = "Alvin"
nuevas_inscripciones = 0
nombre_profe = input( "Ingrese el nombre del profesor: ") #Pedir al usuario que ingrese un nombre, ya se suyo o de alguien mas.
nuevas_inscripciones = int(input("Nuevos almunos: ")) #Pedir al usuario que ingrese un numero, en este caso, la cantidad de nuevos alumnos.

print(type(nombre_profe) is str) #Validar que el nombre ingresado es un string
print(nombre_profe)
print(cantidad_alumnos + int(nuevas_inscripciones)) 
"""Convertir la variable nuevas_inscripciones a entero, ya que input siempre devuelve un string. 
Esto se puede hacer en el momento de escribir el print o desde la fuente del variable"""