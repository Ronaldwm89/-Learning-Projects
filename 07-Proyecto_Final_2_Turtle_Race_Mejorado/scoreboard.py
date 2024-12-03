from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.color("black")
        self.level = 1
        self.write(f"Level {self.level}", False, "left", FONT)


    def game_over(self):
        self.home()
        self.write("G A M E   O V E R", False, "center", FONT)
    
    def act_display(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", False, "left", FONT)