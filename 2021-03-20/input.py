import turtle
    
screen = turtle.Screen()
    
answer = turtle.simpledialog.askstring("Welcome to Bowling!", "Are you ready to bowl?")
    
if answer is None or answer.lower().startswith('n'):
    print("Goodbye!")
    screen.clear()
    screen.bye()
else:
    print("Start!")
