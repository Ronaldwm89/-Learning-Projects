from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("darkgreen")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.timing = 0.1
    
    def move(self):
        self.fd(MOVE_DISTANCE)

    def next_level(self):
        self.timing *= 0.5
        self.goto(STARTING_POSITION)
        