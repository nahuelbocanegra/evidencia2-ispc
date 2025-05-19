from crud_dispositivos import listar_dispositivos,buscar_dispositivos,agregar_dispositivos,eliminar_dispositivos

while True:

    print("\n1 - Listar dispositivo ")
    print("2 - Buscar dispositivo ")
    print("3 - Agregar dispositivo ")
    print("4 - Eliminar dispositivo ")
    print("5 - Salir \n")


    try:
        opcion = int(input("Elija una opcion:   "))
        

        if opcion == 1:
            listar_dispositivos()
        elif opcion == 2:
            dispositivo=input("Ingrese el nombre de dispositivo: ")
            buscar_dispositivos(dispositivo)
        elif opcion == 3:
            dispositivo=input("Ingrese el nombre de dispositivo: ")
            agregar_dispositivos()
        elif opcion == 4:
            dispositivo=input("Ingrese el nombre de dispositivo: ")
            eliminar_dispositivos()
        elif opcion == 5:
            break
        else:
            print("por favor ingrese un numero del 1 al 5")

    except:
        print("Entrada no valida,por favor ingrese un numero del 1 al 5")