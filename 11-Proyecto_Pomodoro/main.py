from tkinter import *
from class_button import Buttons
from class_label import Labels
import math

GREEN = "#9DDE8B"
FONT = "courier"
TEXT_COLOR = "#BFD8AF"
TIME_WORK = 25
BREAK_MIN = 5
BREAK_MAX = 20
repeticiones = 0
cronometro = None

def comenzar_cronometro():
    global repeticiones 
    repeticiones += 1
    print(repeticiones)

    if repeticiones == 8:
        cronometro_regresivo(BREAK_MAX*60)
        label_timer.config(text="Largo Descanso")

    elif repeticiones % 2 != 0:
        cronometro_regresivo(TIME_WORK*60)
        label_timer.config(text="Working")

    else:
        cronometro_regresivo(BREAK_MIN*60)
        label_timer.config(text="Breve Descanso")

def cronometro_regresivo(tiempo): #Funcion que inicia cuenta regresiva del tiempo  
    minutos = math.floor(tiempo / 60)
    segundos = tiempo % 60

    if segundos < 10:
        segundos = f"0{segundos}"
    
    canvas_bg.itemconfig(text_time, text=f"{minutos}:{segundos}")#cambia el texto del cambias, especificamente el timepo

    if tiempo > 0:
        global cronometro
        cronometro = root.after(1000, cronometro_regresivo, tiempo -1)
    else:
        comenzar_cronometro()

        check = ""
        for _ in range(math.floor(repeticiones/2)):
            check += "✔️"
        
        label_check.config(text=check)

def clear():
    global repeticiones
    repeticiones = 0

    root.after_cancel(cronometro)
    canvas_bg.itemconfig(text_time, text="00:00")
    

    label_check.config(text="")
    label_timer.config(text="Timer")


root = Tk()
root.title("Gestor de Tiempo")
root.config(padx=100, pady=50, bg=GREEN)

image_bg = PhotoImage(file=r"Proyecto_Pomodoro\tomato.png")

canvas_bg = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
canvas_bg.create_image(100,110, image=image_bg)
text_time = canvas_bg.create_text(100,130, text ="00:00", fill=TEXT_COLOR, font=(FONT, 24, "bold"))
canvas_bg.grid(column=1, row=1)

label_timer = Labels("Timer", 1,0)
label_check = Labels("", 1,3)

button_start = Buttons("Start", 0,2)
button_start.config(command=comenzar_cronometro)

button_reset = Buttons("Reset", 2,2)
button_reset.config(command=clear)


root.mainloop()





















'''BAKCG="#36BA98"
COLOR_FONT = "#0A6847"
FONT = "Courier"
COLOR_SECOND = "#F6E9B2"

root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=BAKCG)
IMAGE = PhotoImage(file=r"Proyecto_Pomodoro\tomato.png")

canva_bg = Canvas(width=200, height=240, bg=BAKCG, highlightthickness=0)
canva_bg.create_image(100,115, image=IMAGE)
text_time = canva_bg.create_text(100,140, text="00:00", fill=COLOR_SECOND, font=(FONT,24,"bold"))
canva_bg.grid(column=1, row=1)

label_timer = Label(text="Timer", font=(FONT, 24, "bold"), fg=COLOR_SECOND, bg=BAKCG)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", font=(FONT, 14, "bold"), bg=COLOR_SECOND, fg=COLOR_FONT)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", font=(FONT, 14, "bold"), bg=COLOR_SECOND, fg=COLOR_FONT)
button_reset.grid(column=2, row=2)


root.mainloop()


'''



















'''from tkinter import *
import time
import math

PINK = "#B03052"
RED = "#3D0301"
GREEN = "#7ED4AD"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeticiones = 0

def llamar_cronometro():
    trabajo = WORK_MIN * 60
    descanso_corto = SHORT_BREAK_MIN * 60
    descanso_largo = LONG_BREAK_MIN * 60 

    global repeticiones
    repeticiones += 1
    if repeticiones % 2 != 0: 
       cuenta_regresiva(trabajo)
            
    if repeticiones % 2 == 0 and repeticiones != 8:
        cuenta_regresiva(descanso_corto)
            
    if repeticiones == 8:
        cuenta_regresiva(descanso_largo)
        
        
    

def cuenta_regresiva(cuenta):
    
    minutos = math.floor(cuenta / 60)
    segundos = cuenta % 60
    
    if segundos < 10:
        segundos = f"0{segundos}"
         
    canvas.itemconfig(cronometro, text=f"{minutos}:{segundos}")
    if cuenta > 0:
        window.after(1000, cuenta_regresiva, cuenta-1)
    else:
        llamar_cronometro()
   

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)


canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
img_tomato = PhotoImage(file= r"Proyecto_Pomodoro\tomato.png")
canvas.create_image(100,112, image=img_tomato)
cronometro = canvas.create_text(100,130, text="00:00", fill=RED, font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(fg=RED, text="Timer", font=(FONT_NAME, 30, "normal"), bg=GREEN)
label_timer.grid(column=1, row=0)

label = Label(fg=RED, text="✔️", bg=GREEN)
label.grid(column=1, row=3)

button_start = Button(text="Start", width=10, fg=RED, bg=GREEN, highlightthickness=0, command=llamar_cronometro)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", width=10, fg=RED, bg=GREEN, highlightthickness=0)
button_reset.grid(column=2, row=2)




window.mainloop()
'''





































