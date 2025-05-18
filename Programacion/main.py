from crud_dispositivos import listar_dispositivos,buscar_dispositivos,agregar_dispositivos,eliminar_dispositivos

while True:

    print("\n1 - Listar dispositivo ")
    print("2 - Buscar dispositivo ")
    print("3 - Agregar dispositivo ")
    print("4 - Eliminar dispositivo ")
    print("5 - Salir \n")


    opcion = int(input("Elija una opcion:   "))
    

    if opcion == 1:
        listar_dispositivos()
    if opcion == 2:
        dispositivo=input("Ingrese el nombre de dispositivo: ")
        buscar_dispositivos(dispositivo)
    if opcion == 3:
        dispositivo=input("Ingrese el nombre de dispositivo: ")
        agregar_dispositivos()
    if opcion == 4:
        dispositivo=input("Ingrese el nombre de dispositivo: ")
        eliminar_dispositivos()
    if opcion == 5:
        break