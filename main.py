# import colorgram
#
# rgb_colors = []
#
#
# colors = colorgram.extract('blob_image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
"""colorgram was used to extract color palette from a jpg to add to colorlist"""

import turtle as t
import random


color_list = [(248, 238, 219), (223, 155, 90), (214, 240, 228), (240, 206, 90), (104, 170, 203), (36, 109, 149), (199, 227, 239), (113, 193, 161), (153, 61, 94), (208, 78, 109), (243, 215, 226), (25, 134, 101), (224, 81, 59), (205, 133, 155), (184, 59, 43), (177, 166, 36), (138, 219, 198), (39, 54, 113), (238, 161, 180), (105, 40, 73), (137, 215, 228), (239, 168, 157), (14, 93, 69), (60, 166, 132), (27, 47, 88), (53, 157, 186), (109, 116, 170), (72, 36, 65), (14, 69, 51), (180, 186, 218)]
tim = t.Turtle()
tim.hideturtle()
tim.speed(0)
tim.pensize(2)
t.colormode(255)

tim.penup()

def random_color():
    return random.choice(color_list)



def draw_hirst():
    start_x = -300
    start_y = -300

    tim.goto(start_x,start_y)

    for row in range(13):
        for dot in range(13):
            tim.dot(20,random_color())
            tim.forward(50)

        # Move Tim to the beginning of the next upper row
        tim.goto(start_x,start_y +(row + 1) * 50)



draw_hirst()

screen = t.Screen()
screen.exitonclick()