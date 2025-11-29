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
    
def inscribir_en_curso():
    """Inscribir estudiantes al curso"""
    carnet = input("Ingrese el carnet del estudiante (o 'salir'): ")
    if carnet.lower() == "salir":
            return
    if carnet == "":
            print("El carnet no puede estar vacio.")
        
        
        #Validar que el carnet exista
    carnet_existe = False
    for estu in dat.estudiantes:
        if estu["carnet"].lower() == carnet.lower():
            carnet_existe == True
            break
            
        if not carnet_existe:
            print("El carnet no existe. Intente nuevamente.")
            continue
    while True: 
        #Mostrar cursos disponibles
        print("Cursos disponibles: ")
        for codigo in dat.cursos:
            print(codigo, "->", dat.cursos[codigo])
            
        codigo = input("Digite el codigo del curso (o escriba salir): ")
        
        if codigo.lower() == "salir":
            print("Regresando al menú principal")
            continue
        if codigo not in dat.cursos:
            print("Código de curso inválido. Porfavor intentar de nuevo.")
            continue #pedir otro codigo
        ya_inscrito = False
        for insc in dat.inscripciones:
            if insc["carnet"] == carnet and insc["curso"] == codigo:
                ya_inscrito = True
            
            dat.inscripciones.append({
                "carnet": carnet,
                "curso": codigo
            })
            print("Curso inscrito con exito.")
            
            seguir = input("¿Desea inscribir otro curso? (s/n): ")
            if seguir.lower() == "s":
                break