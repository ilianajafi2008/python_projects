# import colorgram
# from pathlib import Path

# image_path = Path(__file__).parent / "image.jpg"
# colors = colorgram.extract(str(image_path), 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r ,g ,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(171, 162, 152), (138, 88, 59), (142, 164, 180), (62, 103, 129), (62, 33, 22), (13, 37, 59), (186, 147, 160), (221, 201, 135), (145, 174, 161), (64, 116, 92), (174, 142, 57), (133, 79, 95), (123, 41, 23), (15, 41, 28), (176, 97, 111), (181, 105, 87), (47, 28, 41), (216, 176, 189), (90, 149, 123), (28, 88, 64), (19, 83, 96), (221, 178, 170), (79, 147, 161), (170, 205, 188), (185, 188, 208), (36, 62, 101)]

import turtle
turtle.colormode(255)
import random
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










screen = turtle.Screen()
screen.exitonclick()

