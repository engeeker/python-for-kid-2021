import turtle
import time
import random

p = turtle.Pen()
p.hideturtle()  # 隐藏箭头
p.color("red")  # 设置画笔颜色

p.penup()
p.goto(0, 200)
p.pendown()

# 无限循环，显示->擦除->显示->擦除.........
while True:
    result = random.choice(['A', 'B', 'C', 'D', 'E'])
    p.write(result, font=("Arial", 40, "normal"))  # 会在坐标 (0, 400) 处显示
    time.sleep(0.1)  # 暂定0.1秒
    p.clear()  # 清理，擦除

turtle.Screen().exitonclick()
