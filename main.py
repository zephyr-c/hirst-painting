import colorgram
import random
import turtle as t
t.colormode(255)
# 10 x 10 rows of spots
# Each dot should be size 20
# Each dot should be spaced apart 50 paces

color_list = [(218, 218, 223), (108, 110, 127), (213, 154, 94), (140, 141, 152), (227, 214, 104),
              (195, 60, 24), (233, 216, 225), (181, 159, 38), (99, 108, 176), (211, 145, 178),
              (200, 17, 5), (24, 23, 69), (25, 43, 24), (34, 37, 15), (227, 167, 198), (220, 82, 55), (42, 43, 108),
              (194, 9, 16), (230, 174, 163), (156, 168, 159), (220, 72, 97), (135, 74, 88), (182, 184, 214),
              (84, 99, 87), (222, 207, 21), (40, 23, 43), (73, 72, 36), (51, 72, 55)]

brush = t.Turtle(visible=False)

# t.setworldcoordinates(-50, -50, 800, 800)

def create_row():
    for _ in range(9):
        brush.color(random.choice(color_list))
        brush.dot(20)
        brush.fd(50)
        brush.dot(20)
brush.speed(0)
brush.pu()
brush.goto(-250, -200)

for _ in range(10):
    create_row()
    y = brush.ycor()
    brush.goto(-250, y + 50)

screen = t.Screen()

screen.exitonclick()