"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
weenr = turtle.Turtle()
def threeDcube():
    for i in range(4):
        weenr.forward(50)
        weenr.right(90)
    weenr.goto(25,25)
    for i in range(4):
        weenr.forward(50)
        weenr.right(90)
    weenr.forward(50)
    weenr.goto(50,0)
    weenr.right(90)
    weenr.forward(50)
    weenr.goto(75,-25)

threeDcube()

"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the file MyFile.py"""

#from MyFile.py import DrawRectangle
















input()
