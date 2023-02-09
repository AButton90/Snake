from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):        
        self.block_list = []
        self.create_snake()
        self.head = self.block_list[0]


    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_block(pos)
    

    def add_block(self, position):
        block = Turtle('square')
        block.color('white')
        block.penup()
        block.goto(position)
        self.block_list.append(block)


    def extend(self):
        self.add_block(self.block_list[-1].position())


    def move(self):
        for i in range(len(self.block_list) - 1, 0, -1):
            new_x = self.block_list[i - 1].xcor()
            new_y = self.block_list[i - 1].ycor()
            self.block_list[i].goto(new_x, new_y)
        self.block_list[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




    