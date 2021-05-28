from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        """Create the food """
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        """Create the food at random places in the canvas"""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

