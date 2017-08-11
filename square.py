import turtle
def draw_square():
    window=turtle.Screen()
    window.bgcolor("yellow")
    square= turtle.Turtle()
    square.forward(100)
    square.right(90)
    square.forward(100)
    square.right(90)
    square.forward(100)
    square.right(90)
    square.forward(100)
    square.right(90)
    window.exitonclick()

draw_square()
