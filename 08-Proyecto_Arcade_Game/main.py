from turtle import Screen
from clase_raqueta import Raqueta
from clase_pelota import Pelota
from clase_dibujar_tabla import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

raqueta_izquierda = Raqueta(-350)
raqueta_derecha = Raqueta(350)  
pelota = Pelota()

score_left = Score((-20,260))
score_right = Score((20,260))


screen.listen()
screen.onkey(raqueta_derecha.right_up, "Up")
screen.onkey(raqueta_derecha.right_down, "Down")
screen.onkey(raqueta_izquierda.left_up, "w")
screen.onkey(raqueta_izquierda.left_down, "s")


start = True
while start:
    screen.update()
    time.sleep(pelota.move_speed)
    pelota.movimiento()

    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.colapso_eje_y()
    
    if pelota.distance(raqueta_derecha) < 50 and pelota.xcor()> 320 or pelota.distance(raqueta_izquierda) < 50 and pelota.xcor() < -320:
        pelota.colapso_raqueta()
    
    if pelota.xcor() > 350:
        score_left.act_score_l()
        pelota.reiniciar()

    if pelota.xcor() < -350:
        score_right.act_score_r()
        pelota.reiniciar()

    if score_right.right_score == 7 or score_left.left_score == 7:
        start = False


screen.exitonclick()


























'''from turtle import Screen
from clase_dibujar_tabla import Tabla
from clase_raqueta import Raquetas
from clase_pelota import Pelota
import time


POS_RAQUETA_LEFT = 350
POS_RAQUETA_RIGHT = -350

start = True

display = Screen()
display.bgcolor("black")
display.setup(800,600)
display.title("Ping Pong")
display.tracer(0)

raqueta_a = Raquetas(POS_RAQUETA_LEFT)
raqueta_b = Raquetas(POS_RAQUETA_RIGHT)


mesa_de_juego = Tabla()
score = Tabla()
score.print_score()
left_player = Tabla()
right_player = Tabla()
mensaje_final = Tabla()



left_player.players()
right_player.players()


pelota = Pelota()

display.listen()
display.onkey(raqueta_a.up, "Up")
display.onkey(raqueta_a.down, "Down")
display.onkey(raqueta_b.up, "w")
display.onkey(raqueta_b.down, "s")



juego_andando = True
while juego_andando:
    display.update()
    time.sleep(pelota.move_speed)
    pelota.movimiento()

    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.rebotar_pared()
        
    if pelota.distance(raqueta_a) < 40 and pelota.xcor()> 320 or pelota.distance(raqueta_b) < 40 and pelota.xcor() < -320:
        pelota.rebotar_raqueta()
        

    if pelota.xcor() > 380:
        left_player.clear()
        left_player.act_scores(POS_SCORE_LEFT)
        juego_andando = False
        pelota.reiniciar_posicion()
        raqueta_a.teleport(POS_RAQUETA_LEFT, 0)
        raqueta_b.teleport(POS_RAQUETA_RIGHT, 0)
        juego_andando = True
    
    if pelota.xcor() < -380:
        right_player.clear()
        right_player.act_scores(POS_SCORE_RIGHT)
        juego_andando = False
        pelota.reiniciar_posicion()
        raqueta_a.teleport(POS_RAQUETA_LEFT, 0)
        raqueta_b.teleport(POS_RAQUETA_RIGHT, 0)
        juego_andando = True

    if left_player.scored == 7 or right_player.scored == 7:
        mensaje_final.mensaje_final()
        juego_andando = False
        
'''
         
'''if pelota.ycor() < -380:
        score_right_player += 1
        break
    right_player.players((20,240), score_right_player)'''
    
    
    
        

    
    
    


display.exitonclick()







'''
from turtle import Screen
from clase_dibujar_tabla import Tabla
from clase_raqueta import Raquetas
import time

display = Screen()
display.bgcolor("black")
display.setup(800,600)
display.title("Ping Pong")
display.tracer(0)

raqueta_a = Raquetas((350, 0))
#raqueta_a.raqueta_derecha()
raqueta_b = Raquetas((-350, 0))
#raqueta_b.raqueta_izquierda()

mesa_de_juego = Tabla()
mesa_de_juego.line_medio()

display.listen()
display.onkey(raqueta_a.up, "Up")
display.onkey(raqueta_a.down, "Down")
display.onkey(raqueta_b.arriba, "w")
display.onkey(raqueta_b.abajo, "s")


juego_andando = True
while juego_andando:
    display.update()
    

    
    


display.exitonclick()'''





















#Juego ping pong

#crear la pantalla
#crear y mover la paleta
#crear otra paleta
#crear la pelota y hacer que se mueva
#detectar cuando la pelota choca con los muros
#detectar cuando la pelota choca con la raqueta
#detectar cuando el jugador anota un punto, cuando la paleta pierde la pelota
#actualizar el puntaje


#crear los scores en variables que vayan aumentando
#dibujar la linea del medio de la tabla
#crear la pelota que se mueva de manera aleatoria pero coherente
#crear las paletas que tenga sensibilidad a las teclas up y down
#crear los pordes de la pantalla para que cuando toque la pelota haya un perdedor/ganador

#los scores deben ir dentro de una misma clase
#las paletas tambien deben tener una misma clase
#la pelota debe tener su propia clase
#el dibujo de la tabla tambien debe tener su propia classe