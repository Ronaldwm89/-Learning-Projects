from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(280, random.randint(-250,250))
        
        
    
    def movimiento(self):
        self.bk(STARTING_MOVE_DISTANCE)
    
    
        


