import turtle


p = turtle.Pen()

#length = int(input("请输入国旗的长度Please input the length："))
#width = int(input("请输入国旗的宽度Please input the width："))
length = int(turtle.textinput('input', "请输入国旗的长度Please input the length："))
width = int(turtle.textinput('input', "请输入国旗的宽度Please input the width："))


# pre-define some variables
# 预先定义一些变量
background_color = "black"
pen_color = ""
fill_color_red = "#AE1C28"
fill_color_white = "#FFFFFF"
fill_color_blue = "#21468B"

turtle.bgcolor(background_color)   # 设置背景颜色为黑色，这个知识点上课我们没有讲过
p.color(pen_color)  # 设置画笔颜色为无色透明， 否则画出的国旗会有一个黑色的边框

p.penup()
p.goto(-250, 250)  # 把画笔移动到屏幕左上角，再开始画
p.pendown()


p.speed(1)  # 可选命令，这个命令可以让画笔走的慢一点，方便大家看清楚画的步骤

# 画第一个长方形
p.fillcolor(fill_color_red)  # 设置第一个长方形的颜色，注意这里不是红色red，而是一种特殊的红色
p.begin_fill()
p.forward(length)
p.right(90)
p.forward(width/3)
p.right(90)
p.forward(length)
p.right(90)
p.forward(width/3)

p.backward(width/3)  # 往后退，并拐弯，为画下一个长方形做准备
p.right(90)
p.end_fill()


# 画第二个长方形
p.fillcolor(fill_color_white)  # 设置第二个长方形的颜色，是白色
p.begin_fill()
p.forward(length)
p.right(90)
p.forward(width/3)
p.right(90)
p.forward(length)
p.right(90)
p.forward(width/3)
p.backward(width/3)
p.right(90)
p.end_fill()

# 画第三个长方形
p.fillcolor(fill_color_blue)  # 设置第三个长方形的颜色，一种特殊的蓝色
p.begin_fill()
p.forward(length)
p.right(90)
p.forward(width/3)
p.right(90)
p.forward(length)
p.right(90)
p.forward(width/3)
p.backward(width/3)
p.right(90)
p.end_fill()
p.hideturtle()   # 用来隐藏turtle的小箭头
