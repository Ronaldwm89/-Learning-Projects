from turtle import Turtle
POSICION_INICIAL =[(0,0),(-20,0),(-40,0)]
MOVER_PASOS = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:

    def __init__(self):
        self.snake_completa = []
        self.create_snake()
        self.cabeza = self.snake_completa[0]

    def create_snake(self):
        for pos in POSICION_INICIAL:    
            self.agregar_segmento(pos)

    def agregar_segmento(self, pos):
        segmento = Turtle("square")
        segmento.color("white")
        segmento.penup()
        segmento.goto(pos)
        self.snake_completa.append(segmento)
    
    def reset_snake(self):
        for seg in self.snake_completa:
            seg.goto(1000,1000)
        self.snake_completa.clear()
        self.create_snake()
        self.cabeza = self.snake_completa[0]


    
    def ampliar_serpiente(self):
        self.agregar_segmento(self.snake_completa[-1].position())
    
    def mover_serpiente(self):
        
        for segmento_serpiente in range(len(self.snake_completa)-1, 0, -1):
            
            new_x = self.snake_completa[segmento_serpiente-1].xcor()
            new_y = self.snake_completa[segmento_serpiente-1].ycor()
            self.snake_completa[segmento_serpiente].goto(new_x, new_y)

        self.cabeza.fd(MOVER_PASOS)
                

    def up(self):
        if self.cabeza.heading() != DOWN:
            self.cabeza.setheading(UP)

    def down(self):
        if self.cabeza.heading() != UP:
            self.cabeza.setheading(DOWN)

    def left(self):
        if self.cabeza.heading() != RIGHT:
            self.cabeza.setheading(LEFT)

    def right(self):
        if self.cabeza.heading() != LEFT:
            self.cabeza.setheading(RIGHT)


        

        