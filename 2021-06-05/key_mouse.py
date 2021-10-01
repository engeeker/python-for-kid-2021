import turtle
import random
screen = turtle.Screen()
screen.tracer(False)
p = turtle.Pen()

def left_click(x, y):
    p.hideturtle()
    p.goto(x, y)

screen.listen()  # 监听任何屏幕上的事件
# 鼠标
screen.onscreenclick(left_click, btn=1)  # 鼠标左键点击，调用函数left_click, 传入鼠标点击点的坐标x,y
while True:
    screen.update()

