import random
import turtle as t

t.bgcolor('yellow')

rups = t.Turtle()
rups.shape('square')
rups.color('red')
rups.speed(0)
rups.penup()
rups.hideturtle()

blad = t.Turtle()
blad_vorm = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('blad', blad_vorm)
blad.shape('blad')
blad.color('green')
blad.penup()
blad.hideturtle()
blad.speed(0)

spel_gestart = False
tekst_turtle = t.Turtle()
tekst_turtle.write('Druk SPATIE om te beginnen', align='center', font=('Arial', 16, 'bold'))
tekst_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)


def buiten_venster():
    muur_links = -t.window_width() / 2
    muur_rechts = t.window_width() / 2
    muur_boven = t.window_height() / 2
    muur_onder = -t.window_height() / 2
    (x, y) = rups.pos()
    buiten = \
        x < muur_links or \
        x > muur_rechts or \
        y < muur_onder or \
        y > muur_boven
    return buiten


def game_over():
    rups.color('yellow')
    blad.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))


def toon_score(huidige_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(huidige_score), align='right', font=('Arial', 40, 'bold'))


def plaats_blad():
    blad.ht()
    blad.setx(random.randint(-200, 200))
    blad.sety(random.randint(-200, 200))
    blad.st()


def start_game():
    global spel_gestart
    if spel_gestart:
        return
    spel_gestart = True

    score = 0
    tekst_turtle.clear()

    rups_snelheid = 1
    rups_lengte = 3
    rups.shapesize(1, rups_lengte, 1)
    rups.showturtle()
    toon_score(score)
    plaats_blad()

    while True:
        rups.forward(rups_snelheid)
        if rups.distance(blad) < 20:
            plaats_blad()
            rups_lengte = rups_lengte + 1
            rups.shapesize(1, rups_lengte, 1)
            rups_snelheid = rups_snelheid + 1
            score = score + 10
            toon_score(score)
        if buiten_venster():
            game_over()
            break


def naar_boven():
    if rups.heading() == 0 or rups.heading() == 180:
        rups.setheading(90)


def naar_onder():
    if rups.heading() == 0 or rups.heading() == 180:
        rups.setheading(270)


def naar_links():
    if rups.heading() == 90 or rups.heading() == 270:
        rups.setheading(180)


def naar_rechts():
    if rups.heading() == 90 or rups.heading() == 270:
        rups.setheading(0)


t.onkey(start_game, 'space')
t.onkey(naar_boven, 'Up')
t.onkey(naar_rechts, 'Right')
t.onkey(naar_onder, 'Down')
t.onkey(naar_links, 'Left')
t.listen()
t.mainloop()
