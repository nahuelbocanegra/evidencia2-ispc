from dispositivos import dispositivos


def listar_dispositivos():
    print("Dispositivos disponibles: ")
    for nombre,datos in dispositivos.items():
        print(f"  - {nombre}")
    
def buscar_dispositivos():
    pass
    
def agregar_dispositivos():
    pass

def eliminar_dispositivos():

     pass

listar_dispositivos()