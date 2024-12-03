from turtle import Turtle

ALINEAR  = "center"
FONT = ("helvetica", 12, "bold")
FONTE = ("arial", 18, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open("C:/Users/ronal/OneDrive/Desktop/Curso100dePython/Proyecto_Snake_Game/data.txt") as file:
            self.high_score = int(file.read())
        
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.pintar_score()


    def pintar_score(self):
        self.clear()
        self.write(f"Score: {self.score} ---  High Score: {self.high_score}", False, ALINEAR, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("C:/Users/ronal/OneDrive/Desktop/Curso100dePython/Proyecto_Snake_Game/data.txt", mode ="w") as file:
             file.write(f"{self.high_score}")

        self.score = 0
        self.pintar_score()
    
    def add_score(self):       
        self.score += 1
        self.pintar_score()


       


    






    '''
    def game_over(self):
        self.goto(0,0)
        self.write("G A M E    O V E R", False, ALINEAR, FONTE)
'''
    
        
