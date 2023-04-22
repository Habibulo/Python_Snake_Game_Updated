from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.turtle_head = self.all_turtle[0]

    def create_snake(self):
        for turtle_index in STARTING_POSITION:
            self.add_new_turtle(turtle_index)
    def add_new_turtle(self, turtle_index):
        new_turtle = Turtle(shape="square")
        new_turtle.shapesize(0.9)
        new_turtle.color("black")
        # new_turtle.speed(100)
        # new_turtle.shapesize(1)
        new_turtle.penup()
        new_turtle.goto(turtle_index)
        self.all_turtle.append(new_turtle)
    def extend(self):
        self.add_new_turtle(self.all_turtle[-1].position())
    def move(self):
        for turtle_seg in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[turtle_seg - 1].xcor()
            new_y = self.all_turtle[turtle_seg - 1].ycor()
            self.all_turtle[turtle_seg].goto(new_x, new_y)
        self.turtle_head.forward(MOVE_DISTANCE)
    def reset_snake(self):
        for i in self.all_turtle:
            i.goto(1000, 1000)
        self.all_turtle.clear()
        self.create_snake()
        self.turtle_head = self.all_turtle[0]
    def right(self):
        if self.turtle_head.heading() != LEFT:
            self.turtle_head.setheading(RIGHT)

    def left(self):
        if self.turtle_head.heading() != RIGHT:
            self.turtle_head.setheading(LEFT)

    def up(self):
        if self.turtle_head.heading() != DOWN:
            self.turtle_head.setheading(UP)

    def down(self):
        if self.turtle_head.heading() != UP:
            self.turtle_head.setheading(DOWN)
