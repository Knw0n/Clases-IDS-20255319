Itemingresar = input("Ingrese el item: ")
print(f"El item ingresado es {Itemingresar}")

"""Palabras y conjuntos de textos == Strings o cadenas de caracteres. 
   Un string no tiene valor o significado numerico. 
   str es un valor de dato y se puede validar (True/False)
   En cadenas de carateres, python los interpreta como arreglos [] (coleccion de elementos),
   es decir, organizando cada caracter como un elemento, comenzando desde el 0. Ej: ABCDE == 01234
   Tambien se pueden usar comillas simples (' ') o triples (''' '''), ademas de las comillas 
   dobles (" "). """
 


my_string = "AAAAABCDEFGHIJ"
letra = int(input("Indique el indice de la letra a mostrar (0-4): "))
print(my_string[letra])

print(len(my_string)) #len = length, es decir, la longitud del string. En este caso, 5 caracteres.
print(my_string[0]) #Acceder al primer caracter del string, en este caso, A.

"""" Indexing(indice): es la posicion de cada caracter en el string, comenzando desde 0.
     Sintaxis: Para acceder a un elemento, utilizamos corchetes [] despues del nombre de la 
     secuencia, y dentro de los corchetes, el numero del indice quer queremos. Ej: my_string[3]"""
     

print(my_string[0:4]) #Desde indice 0 al 3, es decir, ABCD. El indice 4 no se incluye.

"""Rebanada (slicing): es un subconjunto de caracteres dentro de un string"""

print(my_string[1:5:2]) #[Inicio : Fin : Paso]. Paso == Saltos. Desde indice 1 al 4, pero tomando de 2 en 2. En este caso, BDF.


print("H" in my_string) #Validar si un caracter esta dentro del string. Retorna True o False.

print("A"*8) #Repetir un caracter o string.

print(min(my_string)) #Retorna el caracter con el valor ASCII mas bajo. En este caso, A.
print(max(my_string)) #Retorna el caracter con el valor ASCII mas alto. En este caso, J.

print(my_string.count("A")) #Contar cuantas veces aparece un caracter en el string. En este caso, 4.