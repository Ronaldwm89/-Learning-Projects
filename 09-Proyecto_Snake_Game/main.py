from turtle import Screen
from snake_class import Snake
from scoreboard import ScoreBoard
from food import Food
import time
#import random


screen = Screen()
screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


serpiente = Snake()
comida = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(serpiente.up, "Up")
screen.onkey(serpiente.down, "Down") 
screen.onkey(serpiente.left, "Left")
screen.onkey(serpiente.right, "Right") 

comenzar_juego = True
while comenzar_juego:
    screen.update()
    time.sleep(0.2)

    serpiente.mover_serpiente()

    #Detectar cuando la serpiente alcance la comida
    if serpiente.cabeza.distance(comida) < 15:
        serpiente.ampliar_serpiente()
        score_board.add_score()
        comida.nueva_comida()
    #Detectar que la serpiente golpee el borde
    if serpiente.cabeza.xcor() > 290 or serpiente.cabeza.xcor() < -290 or serpiente.cabeza.ycor() > 290 or serpiente.cabeza.ycor() < -290:
        score_board.reset()
        serpiente.reset_snake()
  
    for segmento in serpiente.snake_completa[1:]:
        if serpiente.cabeza.distance(segmento) < 10:
            score_board.reset()
            serpiente.reset_snake()
             

screen.exitonclick()




