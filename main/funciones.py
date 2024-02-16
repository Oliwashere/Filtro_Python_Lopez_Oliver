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

archivo_json="usuarios.json"
archivo2_json="servicios.json"

def guardar_usuario(archivo, datos):
    with open(archivo, 'w') as archivo_json:
        json.dump(datos, archivo_json, indent=2)

def cargar_usuario(archivo):
    try:
        with open(archivo, 'r') as archivo_json:
            datos = json.load(archivo_json)
        return datos
    except FileNotFoundError:
        return []      

def id_usuario(datos):
    ids = [dato.get("id", 0) for dato in datos]
    nuevo_id = max(ids, default=0) + 1
    return nuevo_id    

def id_usuario_name(datos):
    return str(len(datos) + 1)

def mostrar_usuario(archivo):
    datos = cargar_usuario(archivo)

    if not datos:
        print("No hay usuarios registrados.")
        return

    print("Usuarios registrados:")
    print("")
    for lista in datos:
        print(f"Usuario {lista['usuario #']}:")
        for clave, valor in lista.items():
            if clave != 'id' and clave != 'usuario #':
                print(f"  {clave}: {valor}")
        print()

def eliminar_usuario(archivo):
    datos = cargar_usuario(archivo)

    if not datos:
        print("No hay usuarios registrados para eliminar.")
        return

    mostrar_usuario(archivo)

    try:
        numero_lista = int(input("Ingresa el id del usuario que deseas eliminar: "))
        if 1 <= numero_lista <= len(datos):
            lista_eliminada = datos.pop(numero_lista - 1)
            print(f"Usuario {lista_eliminada['usuario #']} eliminado exitosamente.")
            guardar_usuario(archivo, datos)
        else:
            print("Id de usuario inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")

def editar_usuario(archivo):
    datos = cargar_usuario(archivo)

    if not datos:
        print("No hay usuarios creados para editar.")
        return

    mostrar_usuario(archivo)

    try:
        numero_lista = int(input("Ingresa el id del usuario que deseas editar: "))
        if 1 <= numero_lista <= len(datos):
            lista_a_editar = datos[numero_lista - 1]

            print(f"\nUsuario {lista_a_editar['usuario #']}:")
            for clave, valor in lista_a_editar.items():
                if clave != 'id' and clave != 'usuario #':
                    print(f"  {clave}: {valor}")

            for clave in lista_a_editar.keys():
                if clave != 'id' and clave != 'usuario #':
                    nuevo_valor = input(f"Ingrese nuevo valor para {clave}: ")
                    lista_a_editar[clave] = nuevo_valor

            guardar_usuario(archivo, datos)
            print(f"\nUsuario {lista_a_editar['usuario #']} editada exitosamente.")
        else:
            print("Id de usuario inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")        

def guardar_servicio(archivo2, datos):
    with open(archivo2, 'w') as archivo2_json:
        json.dump(datos, archivo2_json, indent=2)

def cargar_servicio(archivo2):
    try:
        with open(archivo2, 'r') as archivo2_json:
            datos = json.load(archivo2_json)
        return datos
    except FileNotFoundError:
        return [] 

def id_servicio(datos):
    ids = [dato.get("id", 0) for dato in datos]
    nuevo_id = max(ids, default=0) + 1
    return nuevo_id    

def id_servicio_name(datos):
    return str(len(datos) + 1)

def mostrar_servicio(archivo2):
    datos = cargar_servicio(archivo2)

    if not datos:
        print("No hay servicios registrados.")
        return

    print("servicios registrados:")
    print("")
    for lista in datos:
        print(f"servicio {lista['servicio #']}:")
        for clave, valor in lista.items():
            if clave != 'id' and clave != 'servicio #':
                print(f"  {clave}: {valor}")
        print()

def editar_servicio(archivo):
    datos = cargar_servicio(archivo)

    if not datos:
        print("No hay servicios creados para editar.")
        return

    mostrar_servicio(archivo)

    try:
        numero_lista = int(input("Ingresa el id del servicio que deseas editar: "))
        if 1 <= numero_lista <= len(datos):
            lista_a_editar = datos[numero_lista - 1]

            print(f"\nServicio{lista_a_editar['servicio #']}:")
            for clave, valor in lista_a_editar.items():
                if clave != 'id' and clave != 'servicio #':
                    print(f"  {clave}: {valor}")

            for clave in lista_a_editar.keys():
                if clave != 'id' and clave != 'servicio #':
                    nuevo_valor = input(f"Ingrese nuevo valor para {clave}: ")
                    lista_a_editar[clave] = nuevo_valor

            guardar_servicio(archivo, datos)
            print(f"\nServicio {lista_a_editar['servicio #']} editado exitosamente.")
        else:
            print("Id de servicio inválido.")
    except ValueError:
        print("Entrada inválida. Ingresa un número.")         


def verif_opcServicios(enunciado, bajo, top):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=top:
                return opcion
            else:
                print(f"Por favor, ingrese una opción válida entre ({bajo}y{top})")
        except ValueError:
            print("Por favor, ingrese una opción válida") 

def crear_servicio(archivo2):

    datos = cargar_servicio(archivo2)

    nuevo_dato = {
        "servicio #": id_servicio_name(datos),
        "nombre": input("Ingresa el nombre del servicio: "),
        "caracteristicas": input("Ingresa las caracteristicas del servicio: "),
        "precio": input("Ingresa el precio del servicio: ")
    }

    datos.append(nuevo_dato)
    guardar_servicio(archivo2, datos)
    print("1. Salir al menú de Gestión de Servicios")
    return archivo2, datos

def crear_usuario(archivo,):

    datos = cargar_usuario(archivo)

    nuevo_dato = {
        "usuario #": id_usuario_name(datos),
        "nombre1": input("Ingresa el primer nombre: "),
        "nombre2": input("Ingresa el segundo nombre: "),
        "apellido1": input("Ingresa el primer apellido: "),
        "apellido2": input("Ingresa el segundo apellido: "),
        "direccion": input("Ingresa la dirección: "),
        "celular": input("Ingresa el número de celular: "),
        "fijo": input("Ingresa el número fijo: "),
        "servicio": "none",
        "tiempo": input("Ingresa s/n si el usuario lleva mas de 10 años con la empresa")
    }

    datos.append(nuevo_dato)
    guardar_usuario(archivo, datos)
    print("1. Salir al menú de Gestión de Usuarios")
    return archivo, datos