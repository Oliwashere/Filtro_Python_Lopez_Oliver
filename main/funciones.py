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
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")    

def verif_opca(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")                

def verif_opcr(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")

def verif_opch(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")                      

def verif_opcp(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")

def verif_opcl(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")   

def verif_opcs(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")          

def verif_opcrep(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida") 

def verif_opcb(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")  

def verif_opci(enunciado,bajo,top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida")                                                           