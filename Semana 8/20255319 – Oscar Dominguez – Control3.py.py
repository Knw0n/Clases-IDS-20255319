agente = "encargado"
platillo = []
precios = []

while True: 
    nombre = input("Ingrese el nombre del agente: ")
    if nombre.lower() == agente:
        break
    else:
        print("Agente no registrado")
        print("Favor ingrese el nombre del agente")
        
while True:
    print("Seleccione una opcion: ")
    print("1.Creación de platillos.")
    print("2.Consulta de platillos y precios.")
    print("3.Colocar un pedido.")
    print("4.Salir")
    pedir = input()
    if pedir == "1":
        nomplatillo = input("Ingrese el nombre del platillo a crear: ")
        precioplatillo = float(input("Ingrese el precio del platillo a crear: "))
        platillo.append(nomplatillo)
        precios.append(precioplatillo)
        print(f"El platillo '{nomplatillo}' con precios {precioplatillo:.2f} ha sido agregado")
            
    elif pedir == "2":
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados.")
            
        else: 
            for i in range(len(platillo)):
                print(f"{platillo[i]}: ${precios[i]:.2f}")
                
    elif pedir == "3":
        if len(platillo)==0:
            print("]No hay platillos disponibles para pedir.")
        else:
            pedido = input("Indique el nombre del platillo para su orden: ").lower()
            encontrado = False
            for i in range(len(platillo)):
                if platillo[i].lower() == pedido:
                    print(f"Usted ha elegido {platillo[i]} con un precio de ${precios[i]:.2f}")
                    encontrado = True
                break
            if not encontrado:
                    print ("El platillo ingresado no existe.")
    
    elif pedir == "4":
        print("Saliendo de la aplicación...")
        break
    
    else: 
        print("Opción no válida, intente de nuevo.")