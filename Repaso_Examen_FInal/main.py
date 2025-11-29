# Este modulo sera el inicio del sistema

import modulo_funciones as fn

while True: 
    print("""
    Bienvenido a nuestro sistema.
    1. Registrar estudiante
    2. Inscribir en curso
    3. Generar reportes
    4. Salir
    """)
    opcion = input("Elija una opcion 1-4: ")
    if opcion == "1":
        fn.registrar_estudiantes()
    elif opcion == "2":
        print("Ha elegido la opcion 2.")
    elif opcion == "3":
        print("Ha elegido la opcion 3.")
    elif opcion == "4":
        print("Gracias por visitarnos.")
        break
    else: 
        print("La opcion elegida no es valida")