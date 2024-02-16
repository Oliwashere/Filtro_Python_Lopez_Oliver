from funciones import *

def menu_principal():
    print("====|¡Bienvenido a la plataforma Movistar!|====")
    print("")
    print("---> Digite el número de la opcion a dar uso <---")
    print("")
    print("1. Menú Administrador")
    print("2. Información del programa")
    print("3. Salir")
    opc=verif_opc("----> ",1,3)
    return opc

def menu_administrador():
    print("====|Menú de Administrador|====")
    print("")
    print("1. Registro y Gestión de Usuarios")
    print("2. Seguimiento del Historial de Usuarios")
    print("3. Personalización de servicios")
    print("4. Gestión de Fidelización de Clientes")
    print("5. Gestión de Servicios")
    print("6. Reportes")
    print("7. Bonificación para Clientes Leales")
    print("5. Salir al menú principal")
    opca=verif_opca("----> ",1,7)
    return opca

def info():
    print("====|Información del programa|====")
    print("")
    print("")
    print("1. Salir al menú principal")
    opci=verif_opci("----> ",1,1)
    return opci

def menu_gest_u():
    print("====|Registro y Gestión de Usuarios|====")
    print("")
    print("1. Crear perfil de Usuario")
    print("2. Ver perfil de Usuario")
    print("3. Actualizar perfil de Usuario")
    print("4. Eliminar perfil de Usuario")
    print("5. Asignación de categorías de Usuario")
    print("6. Salir al menú de Administrador")
    opcr=verif_opcr("----> ",1,6)
    return opcr

def menu_historial_u():
    print("====|Seguimiento del Historial de Usuarios|====")
    print("")
    print("1. Servicios utilizados por Usuarios")
    print("2. Interacciones de Usuarios con la empresa")
    print("3. Salir al menú de Administrador")
    opch=verif_opch("----> ",1,3)
    return opch  

def menu_perso_servicios():
    print("====|Personalización de servicios|====")
    print("")
    print("1. Ofrecimiento de servicios y promos")
    print("2. Patrones de comportamiento de Usuarios")
    print("3. Salir al menú de Administrador")
    opcp=verif_opcp("----> ",1,3)
    return opcp
    
def menu_clientes_leales():
    print("====|Gestión de Fidelización de Clientes|====")
    print("")
    print("1. Seguimiento de Usuarios leales")
    print("2. Bonificaciones")
    print("3. Salir al menú de Administrador")
    opcl=verif_opcl("----> ",1,3)
    return opcl         

def menu_servicios():
    print("====|Gestión de Servicios|====")
    print("")
    print("1. Crear Servicio")
    print("2. Ver Servicios")
    print("3. Actualizar Servicio")
    print("4. Eliminar Servicio")
    print("5. Salir al menú de Administrador")
    opcs=verif_opcs("----> ",1,5)
    return opcs 

def menu_reportes():
    print("====|Reportes|====")
    print("")
    print("1. Informe de Servicios")
    print("2. Salir al menú de Administrador")
    opcrep=verif_opcrep("----> ",1,2)
    return opcrep 

def menu_bonificaciones():
    print("====|Bonificaciones|====")
    print("")
    print("1. Usuarios leales")
    print("2. Asignación de bonificaciones")
    print("3. Eliminación de bonificaciones")
    print("4. Salir al menú de Administrador")
    opcb=verif_opcb("----> ",1,4)
    return opcb 

def menu_crear_usuario(archivo):
    crear_usuario(archivo)

def menu_mostrar_usuario(archivo):
    cargar_usuario(archivo)
    mostrar_usuario(archivo)

def menu_eliminar_usuario(archivo):
    eliminar_usuario(archivo)





