import data_menu
dinero = []

def pago_cafe():
    """Devuelve el valor total de las monedas ingresadas"""
    print("Por favor ingrese su pago en monedas: ")
    quar = int(input("Monedas de 0.25$: "))
    dim = int(input("Monedas de 0.10$: "))
    nick = int(input("Monedas de 0.05$: "))
    pen = int(input("Monedas de 0.01$: "))
    total = round((quar * 0.25 + dim * 0.10 + nick * 0.05 + pen * 0.01), 2)
    return total

def verificar_pago(pago, precio, option):
    cafe = data_menu.names[option]

    if pago > precio:
        print(f"Su pago total fue de ${pago}")
        print(f"El valor del cafe es de ${precio}")
        vuelto = round(pago - precio, 2)
        print(f"recibirá ${vuelto} de cambio!")
        print(f"Su {cafe}☕ esta listo, esperemos que lo disfrutes\n")
    elif pago == precio:
        print(f"Has pagado la cantidad exacta: ${pago}")
        print("No tienes cambio")
        print(f"Su {cafe}☕ esta listo, esperemos que lo disfrutes\n")
    elif pago < precio:
        print("Lo sentimos no tienes suficiente dinero, se te devolveran tus monedas\n\n")

def verificar_recursos(op_c):
    precio_cafe = round(data_menu.MENU[op_c]["cost"], 2)
    recursos_iniciales = data_menu.resources
    recursos_cafe = data_menu.MENU[op_c]["ingredients"]

    for i in recursos_cafe:
        if recursos_iniciales[i] < recursos_cafe[i]:
            print(f"Lo siento no tenemos suficiente {i}\n")
            return

    pago_c = pago_cafe()

    if pago_c >= precio_cafe:
        for i in recursos_cafe:
            recursos_iniciales[i] -= recursos_cafe[i]

    dinero.append(precio_cafe)
    verificar_pago(pago_c, precio_cafe, op_c)

def reporte():
    money = sum(dinero)
    reporte_actual = data_menu.resources
    print("Actualmente los recursos disponibles en nuestro inventario son: ")
    print(f"Water: {reporte_actual['water']}ml\nMilk: {reporte_actual['milk']}ml\nCoffee: {reporte_actual['coffee']}gr\nDinero: {money}$ \n\n")

def iniciar_maquina():
    exit = True
    while exit:
        print("Bienvenido a nuestra maquina de ☕")
        opcion_cliente = input("Que te gustaria tomar? \n1- Espresso \n2- Latte \n3- Capuccino: \n\n").lower()

        if opcion_cliente == "1" or opcion_cliente == "2" or opcion_cliente == "3":
            verificar_recursos(opcion_cliente)
        elif opcion_cliente == "reporte":
            reporte()
        elif opcion_cliente == "apagar":
            exit = False
            print("Apagando la maquina.... OFF")
            break


iniciar_maquina()














'''import data_menu
from data_menu import coins


def inciar_maquina():
    choice = ""
    
    apagar = True
    while apagar:
        
        print("Bienvenido a nuestra maquina de ☕")
        opcion_cliente = input("Que te gustaria tomar? \n1- Espresso \n2- Latte \n3- Capuccino: \n\n").lower()
    
        
        if opcion_cliente == "1" or opcion_cliente == "2" or opcion_cliente == "3":
            monedas(opcion_cliente)
        elif opcion_cliente == "reporte":
            opcion_cliente = 1
            reporte(opcion_cliente)
        elif opcion_cliente == "apagar":
            print("Apagando la maquina.... OFF")
            apagar = False


def monedas(opc):
    valor_c = data_menu.MENU[opc]["cost"]

    print("Por favor ingrese su pago en monedas: ")
    quar = int(input(f"Monedas de 0.25$: "))
    dim = int(input(f"Monedas de 0.10$: "))
    nick = int(input(f"Monedas de 0.05$: "))
    pen = int(input(f"Monedas de 0.01$: "))
    total = (quar*0.25 + dim*0.10 + nick*0.05 + pen*0.01)
    
    print(f"Su pago total fue de {total}$")

    if valor_c > total:
        print("Lo sentimos, no tienes suficiente dinero")
    else:
        print("HI")#preparar_cafe()


            
def reporte(opc):
    c_precio = data_menu.MENU[opc]["cost"]
    c_elegido = data_menu.MENU[opc]["ingredients"]

    print("Su cafe se prepara con:")
    for i in c_elegido:
        print(f"{i}: {c_elegido[i]}")
        print(f"Su cafe espresso tiene un valor de : {c_precio}$")

inciar_maquina() 
'''

'''
Requisitos del programa de máquinas de café

1. Indique al usuario preguntando “¿Qué le gustaría?” (espresso/latte/capuchino):”
a. Verifique la entrada del usuario para decidir qué hacer a continuación.
b. El mensaje debe mostrarse cada vez que se complete la acción, p. una vez que la bebida es
dispensado. El mensaje debería aparecer nuevamente para atender al siguiente cliente.

2. Apague la máquina de café ingresando "apagado" en el mensaje.

a. Para los encargados del mantenimiento de la máquina de café, pueden utilizar “apagado” como palabra secreta para apagar
la máquina. Su código debería finalizar la ejecución cuando esto suceda.

3. Imprimir informe.
a. Cuando el usuario ingresa "informe" en el mensaje, se debe generar un informe que muestre

los valores actuales de los recursos. p.ej.
Agua: 100ml
Leche: 50ml
Café: 76g
Dinero: $2.5

4. ¿Comprueba que hay suficientes recursos?

a. Cuando el usuario elige una bebida, el programa debe comprobar si hay suficientes
recursos para hacer esa bebida.

b. P.ej. si Latte requiere 200 ml de agua pero solo quedan 100 ml en la máquina. No deberia continuar preparando la bebida, sino imprimir: "Lo siento, no hay suficiente agua".
Lo mismo debería suceder si se agota otro recurso, p. leche o café.

5. Procesar monedas.

a. Si hay suficientes recursos para hacer la bebida seleccionada, entonces el programa debe
solicitar al usuario que inserte monedas.
b. Recuerde que veinticinco centavos = $0,25, monedas de diez centavos = $0,10, cinco centavos = $0,05, centavos = $0,01
c. Calcula el valor monetario de las monedas insertadas. P.ej. 1 cuarto, 2 monedas de diez centavos, 1 moneda de cinco centavos, 2
centavos = 0,25 + 0,1 x 2 + 0,05 + 0,01 x 2 = $0,52

6. ¿Verificar la transacción exitosa?
a. Comprueba que el usuario haya insertado suficiente dinero para comprar la bebida que seleccionó.
Por ejemplo, el café con leche cuesta $2,50, pero solo insertaron $0,52 y luego de contar las monedas,
El programa debería decir “Lo siento, no es suficiente dinero. Dinero reembolsado”.

b. Pero si el usuario ha insertado suficiente dinero, entonces el costo de la bebida se agrega al
máquina como ganancia y esto se reflejará la próxima vez que se active el "informe". P.ej.

Agua: 100ml
Leche: 50ml
Café: 76g
Dinero: $2.5

do. Si el usuario ha introducido demasiado dinero, la máquina debería ofrecer cambio.
P.ej. “Aquí hay $2,45 dólares de cambio”. El cambio debe redondearse a 2 decimales.

7. Prepara café.

a. Si la transacción es exitosa y hay suficientes recursos para hacer que la bebida sea la
seleccionado por el usuario, entonces los ingredientes para hacer la bebida deben deducirse del
Recursos para máquinas de café.

P.ej. informe antes de comprar café con leche:
Agua: 300ml
Leche: 200ml
Café: 100g
Dinero: $0

Informe después de comprar café con leche:
Agua: 100ml
Leche: 50ml
Café: 76g
Dinero: $2.5

b. Una vez que se hayan deducido todos los recursos, dígale al usuario “Aquí está tu café con leche. ¡Disfrutar!". Si
el café con leche fue su bebida elegida.
'''