from tkinter import Button
FONT = ("courier", 14, "normal")

class Buttons(Button):
    def __init__(self, text, colums, rows):
        super().__init__()
        self.config(text=text, font= FONT, fg="darkgreen", bg="#9DDE8B")
        self.grid(column=colums, row=rows)

