import turtle    # 导入turtle工具



p = turtle.Pen()   # 创建了一个画笔



point1 = (50, 100)
point2 = (150, 200)

#p.penup()
#p.goto(point1)
#p.pendown()
#p.goto(point2)

#p.hideturtle()
#turtle.exitonclick()
print(p.pos())
p.penup()
p.goto(150, -200)
p.pendown()
p.circle(300)
