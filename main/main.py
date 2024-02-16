from menus import *
from funciones import *

while True:
    clear_screen()
    opc=menu_principal()
    if opc==1:
        clear_screen()
        opca=menu_administrador()
        if opca==1:
            clear_screen()
            opcr=menu_gest_u()
            if opcr==1:
                clear_screen()
                menu_crear_usuario("usuarios.json")
            elif opcr==2:
                clear_screen()
                menu_mostrar_usuario("usuarios.json")    
        elif opca==5:
            clear_screen()
            opcs=menu_servicios()
            if opcs==1:
                crear_servicio("servicios.json")
    elif opc==2:
        clear_screen()
        opc=info()
    elif opc==3:
        clear_screen()
        print("Gracias por usar la plataforma de Movistar")
        print("¡Vuelva pronto!")
        break        
        