#Dicionarios and anidamiento
from art import logo
print(logo)

total_participantes = {}


def ganador():
    oferta = 0
    nombre_ganador = ""


    for key in total_participantes:
        if total_participantes[key] > oferta:
            oferta = total_participantes[key]
            nombre_ganador = key

    print(f"El ganador de la subasta ha sido {nombre_ganador} con un valor en subasta de ${oferta}")

salir = True
while salir:
    nombre = input("Por favor ingresa tu nombre: \n")
    dinero = int(input("Ingrese la cantidad que desea adicionar a la subasta: $ \n"))
    total_participantes[nombre] = dinero
    mas_participantes = input("Hay mas participantes?: Y / N \n")

    if mas_participantes == "N":
        print("Se ha cerrado la subasta")
        salir = False
        ganador()
    elif mas_participantes == "Y":
        print("\n" * 20)



    



























#Segunda clase y ejercicios
'''
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#nested list
travel_log = {
    "France": ["Paris", "Lille","Dijon" ],
    "Germany": ["Stuttgart", "Berlin"]
}

#print lille
print(travel_log["France"][1])

#lista anidada 2d(bidimensional)
lista_anidada = ["A", "B", ["C", "D"], "E"]
print(lista_anidada[2][1])

#anidando diccionarios
travel_logs = {
    "France": {
        "veces_visitado": 5,
        "ciudades_visitadas": ["Paris", "Lille","Dijon"],
        },

    "Germany": {
        "veces_visitado": 5,
        "ciudades_visitadas": ["Stuttgart", "Berlin"],
        },
}

print(travel_logs["Germany"]["ciudades_visitadas"][0])

'''

#Ejercicio de la leccion
'''
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores: 

    if student_scores[key] <= 70:
        student_grades[key] = "Fail"

    elif student_scores[key] >= 71 and student_scores[key] <= 80 : 
        student_grades[key] = "Acceptable"

    elif student_scores[key] >= 81 and student_scores[key] <= 90 : 
        student_grades[key] = "Exceeds Expectations"

    elif student_scores[key] >= 91 and student_scores[key] <= 100 : 
        student_grades[key] = "Outstanding"

print(student_grades)
'''    