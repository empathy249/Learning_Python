from turtle import Turtle, Screen

billy = Turtle()
billy.shape("turtle")
billy.color("coral")
billy.fillcolor("white")
def turn_left (turtle):
    turtle.left(90)

billy.forward(100)
turn_left(billy)
billy.forward(100)
window = Screen()
window.exitonclick()
