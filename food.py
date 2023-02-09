from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 260)
        self.goto(rand_x, rand_y)
