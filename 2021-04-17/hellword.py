import turtle

p = turtle.Pen()
p.speed(0)
color_list = ["red", "green", 'yellow', 'blue']

for i in range(4):
    p.fillcolor(color_list[i])
    p.begin_fill()
    p.circle(100)
    p.left(90)
    p.end_fill()
turtle.Screen().exitonclick()  # click mouse to exit
