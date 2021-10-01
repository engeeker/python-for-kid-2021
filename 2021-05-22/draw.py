import turtle

p = turtle.Pen()
p.speed(0)
size = 20
turtle.Screen().tracer(False)

def cube(p, x, y, color):
    """
    draw a small cube
    :param p: turtle pen
    :param x: x position
    :param y: y postion
    :param color:  fill color
    """
    p.color('grey')
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.fillcolor(color)
    p.begin_fill()
    for i in range(4):
        p.forward(size)
        p.left(90)
    p.end_fill()


metric = [
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 2, 1, 1, 3, 4, 3, 3, 3, 4, 3, 1, 1, 2, 0],
    [0, 0, 0, 1, 3, 4, 3, 3, 3, 4, 3, 1, 0, 0, 0],
    [0, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 0],
    [2, 0, 1, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 0, 2],
    [0, 0, 0, 1, 0, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0]
]

color_map = {
    0: 'white',
    1: '#f6e734',
    2: '#5c6e9d',
    3: '#f7e5d2',
    4: '#1696be',
    5: '#393737'
}

x = 0
y = -20


for i in range(len(metric)):
    y = - (i + 1) * size
    for j in range(len(metric[i])):
        cube(p=p, x=j * size, y=y, color=color_map[metric[i][j]])



























p.hideturtle()
turtle.Screen().exitonclick()
