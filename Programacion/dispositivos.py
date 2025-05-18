dispositivos = {
                "cafetera":{
                    "tipo",
                   "marca",
                    "modelo",       
                    },
                "microondas":{
                    "tipo",
                   "marca",
                    "modelo",  
                },
                "aire acondicionado":{
                    "tipo":111,
                   "marca":111,
                    "modelo":111, 
                    "temperatura media":26
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
    
    opcion=int(input("desea subir o bajar la temperatura (1: subir / 2: bajar): "))

    if opcion == 1 :
        subir_temperatura_aire()
    if opcion == 2 : 
        bajar_temperatura_aire()