from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 360)

first_color = colors[0]

print(first_color.rgb)


def converter(colors):
    for color in colors:
        r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
        if r + g + b < 600:
            bank_colors.append((r, g, b))



bank_colors = []

converter(colors)

print(bank_colors)

redcliff = Turtle()

screen = Screen()
screen.colormode(255)


step_up = -220

for _ in range(0, 10):
    step_forward = -220
    for _ in range(0, 10):
        redcliff.teleport(step_forward, step_up)
        redcliff.dot(20, random.choice(bank_colors))
        step_forward += 50
    step_up += 50















screen.exitonclick()


# def generate_random_color():
#     r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#     return r, g, b


# def draw_polygon(number_of_sides):
#     r, g, b = generate_random_color()
#     redcliff.pencolor(r, g, b)
#
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         redcliff.forward(75)
#         redcliff.left(angle)

# def shampane_walk():
#     r, g, b = generate_random_color()
#     redcliff.pencolor(r, g, b)


# Stay in the current direction
# Turn right from the current direction
# Turn left from the current direction
# Turn 180 degrees from the current direction

# def get_random_direction():
#     options = [0, 90, 180, 270]
#     return random.choice(options)

# screen = Screen()
# screen.colormode(255)
#
# redcliff.pensize(1)
#
# redcliff.speed('fastest')

# for _ in range(250):
#     shampane_walk()
#     redcliff.setheading(get_random_direction())
#     redcliff.forward(50)


# for _ in range(90):
#     redcliff.circle(150)
#     redcliff.color(generate_random_color())
#     redcliff.right(4)
# redcliff.up()
#
#
# redcliff.dot(18, 'darkorchid3')
# redcliff.teleport(60)
# redcliff.dot(18, 'darkorchid3')
# redcliff.teleport(120)
# redcliff.dot(18, 'darkorchid3')
# redcliff.teleport(180)
# redcliff.dot(18, 'darkorchid3')
# redcliff.teleport(240)
# redcliff.dot(18, 'darkorchid3')
# redcliff.teleport(300)
# redcliff.teleport(0, 60)

# number_of_sides = 3
#
# for _ in range(3, 11):
#     draw_polygon(number_of_sides)
#     number_of_sides += 1

# screen.exitonclick()
