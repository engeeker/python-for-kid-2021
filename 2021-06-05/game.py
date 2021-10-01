import turtle
import random
import time

screen = turtle.Screen()
screen_width = 800
screen_height = 600
ball_radius = 20 # 球的半径
ball_color = 'green' # 球的颜色
screen.setup(width=screen_width, height=screen_height)
screen.tracer(False)  # 忽略画图过程，瞬间显示


# 随机在屏幕的上方区域生成坐标x,y ( y > 0的区域）
x = random.randint(-screen_width/2 + ball_radius, screen_width/2 - ball_radius)
y = random.randint(ball_radius, screen_height/2 - ball_radius)

x_speed = 4
y_speed = 4
p = turtle.Pen()
p.hideturtle()


def draw_ball(x, y, p):
    """
    以(x, y)为圆心画一个圆
    :param x: position x
    :param y: position y
    :param p: turtle pen
    :return:
    """
    p.up()
    p.goto(x, y)
    p.color(ball_color)
    p.fillcolor(ball_color)
    p.begin_fill()
    p.circle(ball_radius)
    p.end_fill()

def draw_racket(x, y, width, height, p):
    """
    以(x, y)为长放心的左上顶点，画一个宽width，高height的长方形
    :param x:
    :param y:
    :param width:
    :param height:
    :param p:
    :return:
    """
    p.up()
    p.goto(x, y)


while True:
    draw_ball(x=x, y=y, p=p)
    if y - ball_radius <= - screen_height /2 : # 接触到下边缘
        y_speed = - y_speed                    # y的速度取反
    elif y + ball_radius >= screen_height /2:  # 接触到上边缘
        y_speed = -y_speed                     # y的速度取反
    # 以上两个if语句可以合并成一个

    # 如果x坐标接触到左边缘或者右边缘，则x速度取反
    if x + ball_radius >= screen_width /2 or x - ball_radius <= -screen_width /2:
        x_speed = -x_speed

    x = x + x_speed
    y = y - y_speed
    screen.update()
    p.clear()
    time.sleep(0.1)

