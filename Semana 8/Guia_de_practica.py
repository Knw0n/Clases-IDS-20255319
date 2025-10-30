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

"""EJERCICIO E"""

N = int(input())
Pa = int(input())
Pb = int(input())
Pc = int(input())

for i in range(N):
    combo = input()
    a = combo.count("A")
    b = combo.count("B")
    c = combo.count("C")
    combo1 = Pa*a + Pb*b + Pc*c

print(combo1)  

