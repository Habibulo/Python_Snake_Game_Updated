from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)






    #
    # def __init__(self):
    #     self.food()
    #     self.check_index()
    #     self.position = []
    #     self.food_position()
    #     self.food()
    # def food(self):
    #     create_food = Turtle(shape='square')
    #     create_food.color("red")
    #     create_food.shapesize(0.5)
    # def check_index(self):
    #     for food_index in range(-299, 300):
    #         self.position.append(food_index)
    # def food_cor(self):
    #     coordination = []
    #     x = self.food.xcor(random.choice(self.position))
    #     y = self.food.ycor(random.choice(self.position))
    #     coordination.append(x, y)
    # def food_position(self):
    #     self.food().goto(self.food_cor())
