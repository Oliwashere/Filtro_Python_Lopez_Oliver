import os
import json

def clear_screen():
    os.system("cls"if os.name == "nt" else "clear")

def verif_opc(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"La opcion no se encuetra entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")    