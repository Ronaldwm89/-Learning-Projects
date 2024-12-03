import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
start = 0
carros = []
while game_is_on:
    

    time.sleep(player.timing)
    screen.update()
    if start == 6:
        start = 0
        car = CarManager()
        carros.append(car)
    
    for cart in carros:
        cart.movimiento()

        if cart.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        
        if player.ycor() > 280:
            scoreboard.act_display()
            player.next_level()

    start += 1
    

screen.exitonclick()