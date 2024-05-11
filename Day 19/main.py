import turtle as turtelerino


screen = turtelerino.Screen()
screen.setup(width=500, height=400)

rainbow_turtles = ['red', 'orange', 'yellow', 'green', 'blue',]
turtle_names = ['redcliff', 'tommy', 'timmy', 'johnny', 'benny']


redcliff = turtelerino.Turtle(shape='turtle')
tommy = turtelerino.Turtle(shape='turtle')
timmy = turtelerino.Turtle(shape='turtle')
johnny = turtelerino.Turtle(shape='turtle')
benny = turtelerino.Turtle(shape='turtle')




redcliff.penup()
redcliff.goto(-230, -125)

screen.exitonclick()
