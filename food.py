from turtle import Turtle
import random


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    rgb = (r, g, b)
    return rgb


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random_color())
        self.speed("fastest")
        # self.score = -1
        self.refresh()

    def refresh(self):
        self.color(random_color())
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        # self.score += 1
