import turtle

# Create the drawing pen
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(3)


def draw_clock(hr, mn, sec, pen):

    # Draw clock face
    pen.up()
    pen.goto(0, 210)   # 为了让圆心的位置是(0, 0)
    pen.setheading(180)   # 让箭头指向 180度方向，也就是 <-
    # 各种箭头的方向
    # -> 0 度
    # ^  90度
    # <- 180度
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # Draw hour hashes
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)   # 90度方向，也就是箭头朝上

    for _ in range(12):
        pen.forward(190)
        pen.pendown()
        pen.forward(20)  # 20长度的表盘刻度
        pen.penup()
        pen.goto(0, 0)
        pen.right(30)

    # Draw the hands
    # Each tuple in list hands describes the color, the length
    # and the divisor for the angle
    hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
    # ("white", 80, 12) 代表时针，白色，长度80，12代表360度分成12份
    time_set = (hr, mn, sec)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360   # 如果画时针6点，就是 (6/12)*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)  # 让箭头朝上
        pen.right(angle)
        pen.pendown()
        pen.forward(hand[1])



draw_clock(hr=6, mn=20, sec=45, pen=pen)
turtle.bgcolor("black")
pen.hideturtle()
turtle.Screen().exitonclick()