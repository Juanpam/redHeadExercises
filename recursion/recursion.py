# Module import
import turtle

def branch(turtle,length, angle):
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length/2)
    turtle.backward(length/2)
    turtle.left(angle)
    turtle.left(angle)
    turtle.forward(length/2)
    turtle.backward(length/2)
    turtle.right(angle)

def tree(turtle, length, angle):
    rate = 1 / 2
    minLength = 1
    if(length >= minLength):
        turtle.forward(length)
        turtle.right(angle)
        tree(turtle, length * rate, angle)
        turtle.left(2 * angle)
        tree(turtle, length * rate, angle)
        turtle.right(angle)
        turtle.backward(length)
# To-do
def spiral():
    return

def initialize():
    # Creates turtle as an object
    myTurtle = turtle.Turtle()
    # Creates the screen as an object
    myScreen = turtle.Screen()
    # Assigns the turtle a shape
    myTurtle.shape("turtle")
    

    myTurtle.left(90)
    # branch(myTurtle, 80, 30)
    tree(myTurtle, 240, 20)

    # So the screen waits till a click ocurrs to finish execution
    myScreen.exitonclick()

# Checks if the given module is the main module
if __name__ == '__main__':
    initialize()


