import turtle
def draw_square(new_square):

    for i in range(1,5):
        new_square.forward(100)
        new_square.right(90)

def draw_circle():
    window=turtle.Screen()
    window.bgcolor("yellow")
    square= turtle.Turtle()
    for i in range(1,37):
        draw_square(square)
        square.right(10)
    window.exitonclick()
draw_circle()
