dispositivos = {
        "microondas": {
            "tipo": "Microondas con grill",
            "marca": "Panasonic",
            "modelo": "NN-GT68KS"
        },
        "aire_acondicionado": {
            "tipo": "Split Inverter",
            "marca": "LG",
            "modelo": "DualCool Artcool",
            "temperatura media": 20
        },
        "cafetera": {
            "tipo": "Cafetera espresso automática",
            "marca": "De'Longhi",
            "modelo": "Magnifica S ECAM 22.110.B"
        }
}


def subir_temperatura_aire():
    temperatura=dispositivos["aire acondicionado"]["temperatura media"] 
    if temperatura < 32:
        temperatura +=1

def bajar_temperatura_aire():
    temperatura=dispositivos["aire acondicionado"]["temperatura media"] 
    if temperatura > 15:
        temperatura -= 1

def control_aire():

    try:

        opcion=int(input("desea subir o bajar la temperatura (1: subir / 2: bajar): "))

        if opcion == 1 :
            subir_temperatura_aire()
        elif opcion == 2 : 
            bajar_temperatura_aire()
        else:
          print("por favor ingrese un numero del 1 al 2")

    except:
        print("Entrada no valida,por favor ingrese un numero del 1 al 2")