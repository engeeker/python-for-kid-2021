import turtle
import time

screen = turtle.Screen()
screen.tracer(False)
screen_width = screen.window_width()
pen = turtle.Pen()
pen.hideturtle()

x = 0
y = 0
tree_x = 0

def draw_car(x, y, pen, angle):

    # Below code for drawing rectangular upper body  画一个红色车身
    pen.color('red')
    pen.fillcolor('red')
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(370)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    # Below code for drawing window and roof  画车顶和窗户
    pen.penup()
    pen.goto(x+100, y+50)
    pen.pendown()
    pen.setheading(45)
    pen.forward(70)
    pen.setheading(0)
    pen.forward(100)
    pen.setheading(-45)
    pen.forward(70)
    pen.setheading(90)
    pen.penup()
    pen.goto(x+ 200, y+ 50)
    pen.pendown()
    pen.forward(49.50)

    # Below code for drawing two tyres  两个轮子
    pen.penup()
    pen.goto(x+100, y-10)
    pen.pendown()
    pen.color('black')
    pen.fillcolor('white')
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    pen.penup()
    pen.goto(x+300, y-10)
    pen.pendown()
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

def draw_tree(x, y, pen):

    for distance in [-300, -100, 100, 250, 400, 500]:
        pen.penup()
        pen.goto(x + distance, y)
        pen.pendown()
        pen.setheading(90)
        pen.forward(200)
        pen.backward(50)
        pen.left(30)
        pen.forward(50)
        pen.backward(50)
        pen.right(70)
        pen.forward(50)


while True:
    draw_tree(tree_x, y-30, pen)
    tree_x = tree_x + 10
    pen.setheading(0)
    draw_car(x, y, pen, 10)
    # draw road
    pen.color('black')
    pen.penup()
    pen.goto(-screen_width/2, y-30)
    pen.setheading(0)
    pen.pendown()
    pen.forward(screen_width)
    screen.update()
    #x = x - 10
    pen.clear()
    time.sleep(0.1)

