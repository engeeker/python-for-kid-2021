import turtle
import time
import datetime

def draw_clock(hr, mn, sec, pen):
    """

    :param hr: 当前的小时
    :param mn: 当前的分钟
    :param sec: 当前秒
    :param pen: 画笔
    :return:
    """

    # Draw clock face 画表盘
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)   # 箭头指向9点钟方向
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # Draw hour hashes 画刻度
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)  #箭头指向12点钟方向

    for _ in range(12):
        pen.forward(190)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.goto(0, 0)
        pen.right(30)

    # 时针的颜色，长度和角度
    hour_hand_color = 'white'
    hour_hand_length = 80
    hour_hand_angle = (hr / 12) * 360  # 距离12点种方向偏离的角度

    # 画时针
    pen.penup()
    pen.goto(0, 0)
    pen.color(hour_hand_color)
    pen.setheading(90)
    pen.right(hour_hand_angle)
    pen.pendown()
    pen.forward(hour_hand_length)

    # 分针的颜色，长度和角度
    minute_hand_color = "blue"
    minute_hand_length = 150
    minute_hand_angle = (mn / 60) * 360

    # 画分针
    pen.penup()
    pen.goto(0, 0)
    pen.color(minute_hand_color)
    pen.setheading(90)
    pen.right(minute_hand_angle)
    pen.pendown()
    pen.forward(minute_hand_length)

    # 秒针的颜色，长度和角度
    second_hand_color = "red"
    second_hand_length = 110
    second_hand_angle = (sec / 60) * 360

    # 画秒针
    pen.penup()
    pen.goto(0, 0)
    pen.color(second_hand_color)
    pen.setheading(90)
    pen.right(second_hand_angle)
    pen.pendown()
    pen.forward(second_hand_length)



screen = turtle.Screen()
screen.bgcolor("black")  # 设置背景颜色
screen.tracer(False)
# Create the drawing pen
pen = turtle.Pen()
pen.hideturtle()  # 隐藏箭头
pen.width(3)  # 画笔粗度


while True:
    now = datetime.datetime.now()  # 获取当前时间
    hr = now.hour
    mn = now.minute
    sec = now.second
    draw_clock(hr, mn, sec, pen) # 画
    time.sleep(1)
    screen.update() # screen 更新
    pen.clear()
