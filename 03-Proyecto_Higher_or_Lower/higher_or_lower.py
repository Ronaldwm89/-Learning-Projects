import random
import art
from game_data import data

print(art.logo)

def indice():
    #Indice aleatorio necesario para imprimir diferentes personajes
    index = random.randint(0, len(list(data))-1)
    return index

def personaje():
    #Retorna un personaje aleatorio
    persona = list(data[indice()].values())
    return persona

def imprimir_personaje(x):
    #imprime cada uno de los personajes en el formato deseado
    persona_x = personaje()
    print(f"El personaje {x} es: {persona_x[0]} un {persona_x[2]} que nacio en {persona_x[3]}")

    return persona_x

def pantalla_inicial():
    per_a = imprimir_personaje("A")
    print(art.versus)
    per_b = imprimir_personaje("B")
       
    jugar(per_a, per_b, 0)
   
def continua_jugando(pa, pt):
    
    print(f"El personaje A es: {pa[0]} un {pa[2]} que nacio en {pa[3]}")
    print(art.versus)
    pb = imprimir_personaje("B")

    jugar(pa, pb, pt)

def mensaje_final(p):
    print("\n" * 10)
    print(art.logo)
    print(f"Perdiste, alcanzaste una puntuacion de {p} puntos")
    print(art.triste)
    print("\n" * 10)
    
def jugar(persona_a, persona_b, pts):   
    exit = True
    while exit:
        
        opcion = input("Ingresa cual de las dos opciones crees que tiene mas seguidores: A or B: ").upper()
    
        if opcion == "A": 
            if persona_a[1] > persona_b[1]:
                pts += 1
                print("\n" * 20)
                print(art.logo)
                print(f"Correcto total {pts} punto")
                continua_jugando(persona_b, pts)
            else:
                mensaje_final(pts)
                break
            
        if opcion == "B": 
            if persona_b[1] > persona_a[1]:
                pts += 1
                print("\n" * 20)
                print(art.logo)
                print(f"Correcto total {pts} punto")
                continua_jugando(persona_b, pts)
            else:
                mensaje_final(pts)
                break
             
        exit = False

    

pantalla_inicial()
   

