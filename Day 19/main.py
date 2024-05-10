import turtle as turtelerino

redcliff = turtelerino.Turtle()

screen = turtelerino.Screen()


def move_forward():
    redcliff.forward(100)

screen.listen()
screen.onkey(key='w', fun=move_forward)


screen.exitonclick()