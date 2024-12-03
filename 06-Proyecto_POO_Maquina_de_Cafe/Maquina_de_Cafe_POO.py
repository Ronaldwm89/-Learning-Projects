from operator import getitem, invert

import menu
from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu() #Objeto de la clase Menu
maquina_monedas = MoneyMachine() #Objeto de la clase MoneyMachine
maquina_cafe = CoffeeMaker() #objeto de la clase CoffeMaker

opciones_menu = menu.get_items() #obtener los itens desde la instancia Menu de la clase MenuItem

exit = True
while exit:
    print("Bienvenido a nuestra maquina de Cafe ☕")
    opcion_usuario = input(f"Por favor escoja una de las opciones del menu\n{opciones_menu}:\n")


    if opcion_usuario == "report":
        maquina_cafe.report()
        maquina_monedas.report()
    elif opcion_usuario == "off":
        exit = False
    else:
        verificar_bebida = menu.find_drink(opcion_usuario)
        if verificar_bebida.name:

            precio_bebida = verificar_bebida.cost
            recursos_bebida = maquina_cafe.is_resource_sufficient
            if recursos_bebida(verificar_bebida):
                hacer_pago = maquina_monedas.make_payment(precio_bebida)
                if hacer_pago:
                    inventario = maquina_cafe.make_coffee(verificar_bebida)



