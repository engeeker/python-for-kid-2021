import turtle
import random

p = turtle.Pen()
color_list = ['red', 'yellow', 'blue', 'green']
p.speed(0)
turtle.bgcolor('black')
p.color(random.choice(color_list))

for i in range(200):
    p.forward(i * 2)
    p.left(91)

turtle.Screen().exitonclick()