from mimetypes import init
from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'
STYLE = 'normal'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color('white')
        self.penup()
        self.goto(0,275)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(arg = f'Score: {self.current_score}', move = False, align = ALIGNMENT, font = (FONT, 14, STYLE))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg = 'Game Over', move = False, align = ALIGNMENT, font = (FONT, 16, STYLE))

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write_score()
        

    