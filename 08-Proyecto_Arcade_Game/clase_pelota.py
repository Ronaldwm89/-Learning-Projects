from turtle import Turtle

class Pelota(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.mover_x = 10
        self.mover_y = 10
        self.move_speed = 0.1
        

    def movimiento(self):
        eje_x = self.xcor() + self.mover_x
        eje_y = self.ycor() + self.mover_y
        self.goto(eje_x, eje_y)
    
    def colapso_eje_y(self):
        self.mover_y *= -1
    
    def colapso_raqueta(self):
        self.mover_x *= -1
        self.move_speed *= 0.9
    
    def reiniciar(self):
        self.home()
        self.mover_x *= -1
        self.move_speed = 0.1
        
































'''from turtle import Turtle


class Pelota(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5,0.5)
        self.penup()
        self.direccion_y = 10
        self.direccion_x = 10
        self.move_speed = 0.1

    def movimiento(self):
        eje_y = self.ycor() + self.direccion_y
        eje_x = self.xcor() + self.direccion_x
        self.goto(eje_x, eje_y)
    
    def rebotar_pared(self):
        self.direccion_y *= -1
    
    def rebotar_raqueta(self):
        self.direccion_x *= -1
        self.move_speed *= 0.9
        
    def reiniciar_posicion(self):
        self.home()
        self.move_speed = 0.1
        self.rebotar_raqueta()

 '''




        


