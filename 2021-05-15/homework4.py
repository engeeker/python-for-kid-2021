import turtle
import random

p = turtle.Pen()
color_list = ['red', 'yellow', 'blue', 'green']
p.speed(0)
turtle.bgcolor('black')


height = turtle.window_height()
width = turtle.window_width()

for j in range(20):
    x = random.randint(-width / 2, width / 2)
    y = random.randint(-height / 2, height / 2)
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.color(random.choice(color_list))
    size = random.randint(20, 100)
    for i in range(size):
        p.forward(i * 2)
        p.left(91)

turtle.Screen().exitonclick()