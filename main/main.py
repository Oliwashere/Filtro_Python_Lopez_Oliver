from menus import *
from funciones import *

while True:
    clear_screen()
    opc=menu_principal()
    if opc==1:
        clear_screen()
        opca=menu_administrador()
    elif opc==2:
        clear_screen()
        opci=info()
    elif opc==3:
        clear_screen()
        print("Gracias por usar la plataforma de Movistar")
        print("¡Vuelva pronto!")
        break        
        