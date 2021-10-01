import turtle
import random
import time

turtle.hideturtle()
p = turtle.Pen()
p.hideturtle()
screen = turtle.Screen()
screen.tracer(False)

state_num = 0
global name

name_list = ['A', 'B', 'C', 'D', 'E']
name = random.choice(name_list)


def advance_state_machine():
    global state_num
    if state_num == 0:
        state_num = 1
    else:
        state_num = 0


screen.onkey(advance_state_machine, "space")

screen.listen()
while True:
    if state_num == 0:
        name = random.choice(name_list)
    p.write(name, font=("Arial", 100, "normal"))
    time.sleep(0.01)  # 暂定0.01秒
    p.clear()  # 清理，擦除
