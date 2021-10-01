import turtle

p = turtle.Pen()
height = turtle.window_height()
width = turtle.window_width()
print(height)
print(width)

p.goto(100000, 20000000)

turtle.Screen().exitonclick()