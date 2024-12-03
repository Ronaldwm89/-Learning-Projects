import random
from art_adivina import logo_adivina  

numeros = list(range(1, 101))
numero_aleatorio = 0

def mensajes(chance):
    if chance > 0:
        print(f"Te quedan {chance} oportunidades")
        print("\n")
    if chance == 0:
        print("Lo sentimos, perdiste! Te quedaste sin oportunidades")

def adivinador(num, intentos):
    while intentos != 0:
        num_jugador = int(input("Ingresa el numero que creas que es: \n"))
        if num_jugador == num:
            print("Ganaste!! Lo has advinado")
            break

        elif num_jugador > num:
            print("Tu numero es muy alto")
            intentos -= 1
            mensajes(intentos)
          

        elif num_jugador < num:
            print("Tu numero es muy bajo")
            intentos -= 1
            mensajes(intentos)
           
def numero_y_dificultad(opc):
    numero_aleatorio = random.choice(numeros)
    chance = 0
    if opc == "1":
        chance += 12
        print(f"Comencemos tienes {chance} oportunidades")

    elif opc == "2":
        chance += 8
        print(f"Comencemos tienes {chance} oportunidades")

    elif opc == "3":
        chance += 5
        print(f"Comencemos tienes {chance} oportunidades")
    else:
        print("Debes elegir una opcion valida entre (1-3)")
    adivinador(numero_aleatorio, chance)


print("\n")
print("Bienvenido al juego Adivina el Numero!!")
print(logo_adivina)
print("\n")
print("Listo!! Ya pense en un numero del 1 al 100: ")
print("Ahora, para comenzar, debes elegir la dificultad")
opcion = input("\n 1- Facil \n 2- Medio \n 3- Dificil: \n ")

numero_y_dificultad(opcion)

