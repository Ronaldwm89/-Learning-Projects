from turtle import Turtle
FONT_SCORE = ("helvetica", 24, "normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(0, False, "center", FONT_SCORE)
        self.left_score = 0
        self.right_score = 0
        
    def act_score_l(self):
        self.left_score += 1
        self.clear()
        self.write(self.left_score, False, "center", FONT_SCORE)
    
    def act_score_r(self):
        self.right_score += 1
        self.clear()
        self.write(self.right_score, False, "center", FONT_SCORE)

        
































'''from turtle import Turtle

POS_SCORE_LEFT = (-20,240)
POS_SCORE_RIGHT = (20,240)
FUENTE = ("Comic Sans", 18, "bold")
FUENTE_SCORES = ("Comic Sans", 24, "bold")


class Tabla(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.teleport(0,300)
        self.color("white")
        self.right(90)
        self.goto(0,-300)
        self.l_score = 0
        self.r_score = 0

    def print_score(self):
        self.penup()
        self.goto(0, 270)
        self.write("SCORE", False, "center", FUENTE)
    
    def players(self, position):
        self.penup()
        self.goto(position)
        self.write(self.scored, False, "center", FUENTE)

    def act_scores_left(self):
        self.l_score += 1
        self.clear()
        self.penup()
        self.goto(POS_SCORE_LEFT)
        self.write(self.l_score, False, "center", FUENTE)
    
    def act_scores_right(self):
        self.r_score += 1
        self.clear()
        self.penup()
        self.goto(POS_SCORE_RIGHT)
        self.write(self.r_score, False, "center", FUENTE)


    def mensaje_final(self):
        self.clear()
        self.home()
        self.write("Termino el juego tenemos un ganador!!", False, "center", FUENTE_SCORES)
            
        




'''