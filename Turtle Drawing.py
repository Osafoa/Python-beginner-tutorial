# Let's  draw some cool drawings with the  package turtle

# Import turtle
import turtle

# let's get a nice set-up in turtle
turtle.bgcolor("black")  # Background color
turtle.pensize(2)  # Pen size
turtle.color('red')
turtle.speed(0)

# Draw a square
# turtle.forward(50)  # moves forward
# turtle.left(90)   # moves left 90 degrees
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done() # Allows turtle to stay on the screen

# Nice little project in turtle- creates a nice graph
# for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colors)
#     turtle.circle(150)
#     turtle.left(10)


# Let's make it cooler
for i in range(6):
    for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(10)
turtle.done()

