# Vamos a construir las funciones del sistema
import modulo_datos as dat


def registrar_estudiantes():
    """Validará u registrará estudiantes."""
    while True:
        carnet_i = input("Digite el numero de carnet: ")
        largo_carnet = len(carnet_i)
        existe = False
        for estu in dat.estudiantes:
            if estu["carnet"] == carnet_i:
                existe = True
        if largo_carnet >= 6 and largo_carnet <= 10 and existe == False:
            break
        else: 
            print("El carnet no tiene lo largo esperado")
    
    while True: 
        nombre_i = input("Digite el nombre: ")
        if len(nombre_i) > 1:
            break
        else:
            print("El nombre no tiene lo largo requerido.")
    while True:
        apellido_i = input("Digite el apellido: ")
        if len(apellido_i) > 1:
            break
        else:
            print("El apellido no tiene lo largo requerido.")
            
    dat.estudiantes.append({
        "carnet": carnet_i,
        "nombre": nombre_i,
        "apellido": apellido_i
    })
        