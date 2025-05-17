from dispositivos import dispositivos

def listar_dispositivos():
    
    print("Dispositivos disponibles: ")

    for nombre in dispositivos.keys():
        print(f"  - {nombre}")
    
def buscar_dispositivos(dispositivo):
   
    if dispositivos[dispositivo]:
        return dispositivos[dispositivo]
    else:
        return " no se ha encuentrado el dispositivo "
    
    
def agregar_dispositivos(nuevo_dispositivo,listar_dispositivos):

    if  nuevo_dispositivo in dispositivos:
       print(" ya se encuentra este dispositivo ")
    else:
        dispositivos[nuevo_dispositivo]={ }

    listar_dispositivos()

def eliminar_dispositivos(dispositivo_eliminado,listar_dispositivos):
    pass