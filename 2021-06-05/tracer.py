import turtle

p = turtle.Pen()
turtle.Screen().tracer(False)
for _ in range(20):
    p.circle(100)
    p.left(18)
turtle.Screen().exitonclick()


