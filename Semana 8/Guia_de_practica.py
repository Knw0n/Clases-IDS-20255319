""" EJERCICIO A

numero = int(input())

if numero > 0:
    print ("Positivo")
else:
    print ("Negativo")
    
"""

#########################################

""" EJERCICIO B

numero = int(input())

if numero % 2 == 0:
    print(numero + 2)
    print(numero - 1)
else:
    print(numero + 1)
    print(numero - 2)
    
"""
    
#########################################

"""EJERCICIO C

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

notas = [n1, n2, n3, n4, n5, n6]

if sum(notas)/6 > 9.5:
    print("Gana Premio :)")
else: 
    print("No Gana Premio :(")
"""

##########################################

"""EJERCICIO D

N = int(input())
cont7 = 0
cont5 = 0

for i in range(N):
    num = int(input())
    if num == 7:
        cont7 += 1
    elif num == 5:
        cont5 += 1
print(cont7, cont5)

"""

##########################################

"""EJERCICIO E

N = int(input())
datos = input().split()
Pa = int(datos[0])
Pb = int(datos[1])
Pc = int(datos[2])

for i in range(N):
    combo = input()
    a = combo.count("A")
    b = combo.count("B")
    c = combo.count("C")
    print(Pa*a + Pb*b + Pc*c)
"""

##########################################

"""EJERCICIO F

N = int(input())

for i in range(N):
    
    nombre = input()
    if len(nombre) <= 6: 
        print("No vale la pena")
        
    elif len(nombre) >= 8:
        print("Si aguanto otro desarrollo de personaje")
        
    else:
        print("Dios no creo aguantar esta vez")
"""

##########################################

"""EJERCICIO G

nums = input().split()
x = int(nums[0])
y = int(nums[1])
if x > y:
    print(x)
elif x < y:
    print(y)
else:
    print(x)
"""

##########################################

"""EJERCICIO H

A = int(input())
entrar = 0
for i in range(A):
    edad = int(input())
    if edad >= 15:
        entrar += 1
print(entrar)
"""

##########################################

""" EJERCICIO I

status = input()

if len(status) <= 9:
    print("Ola Ivan")
else: 
    print("Ol..")

"""

##########################################

"""EJERCICIO J

N = int(input())

for i in range(N):
    P = int(input())
    if P >= 3:
        print("Ok")
    else: 
        print("No")
"""