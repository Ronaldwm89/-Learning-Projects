from turtle import Turtle



class Raqueta(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.goto(position,0)
        

    def right_up(self):
        eje_y = self.ycor() + 20
        self.goto(self.xcor(), eje_y)

    def right_down(self):
        eje_y = self.ycor() - 20
        self.goto(self.xcor(), eje_y)

    def left_up(self):
        eje_y = self.ycor() + 20
        self.goto(self.xcor(), eje_y)

    def left_down(self):
        eje_y = self.ycor() - 20
        self.goto(self.xcor(), eje_y)























'''from turtle import Turtle

class Raquetas(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)  
        self.penup()
        self.goto(position,0)
        
 
    def up(self):
        eje_y = self.ycor() + 20
        self.goto(self.xcor(), eje_y)

    def down(self):
        eje_y = self.ycor() - 20
        self.goto(self.xcor(), eje_y)
    

        '''
        
'''

    #def down():'''

'''    
POSITION_RAQUETA_A = 350
POSITION_RAQUETA_B = -350

class Raquetas:
    def __init__(self):
        self.raquet = Turtle("square")
        self.raquet.color("white")
        self.raquet.shapesize(5,1)  

    def raqueta_derecha(self):
        self.raquet.teleport(POSITION_RAQUETA_A,0)
    
    def raqueta_izquierda(self):
        self.raquet.teleport(POSITION_RAQUETA_B,0)
 
    def up(self):
        eje_y = self.raquet.ycor() + 20
        self.raquet.teleport(POSITION_RAQUETA_A,eje_y)

    def down(self):
        eje_y = self.raquet.ycor() - 20
        self.raquet.teleport(POSITION_RAQUETA_A,eje_y)

    def arriba(self):
        eje_y = self.raquet.ycor() + 20
        self.raquet.teleport(POSITION_RAQUETA_B,eje_y)

    def abajo(self):
        eje_y = self.raquet.ycor() - 20
        self.raquet.teleport(POSITION_RAQUETA_B,eje_y)
        
        '''
